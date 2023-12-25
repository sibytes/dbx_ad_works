# Databricks notebook source
# MAGIC %md
# MAGIC # Main Entry Point for a Table Load Task
# MAGIC
# MAGIC This default notebook is executed using Databricks Workflows as defined in resources/ingest_ad_works_job.yml.

# COMMAND ----------

# MAGIC %pip install pyyaml
# MAGIC

# COMMAND ----------

dbutils.widgets.text("process_id", "-1", "process_id")
dbutils.widgets.text("table", "person_business_entity_address", "table")
dbutils.widgets.text("load_type", "default", "load_type")

# stage load parameters
dbutils.widgets.text("force", "false", "force")
dbutils.widgets.text("stage_merge_schema", "true", "stage_merge_schema")
dbutils.widgets.text("modified_after", "", "modified_after")
dbutils.widgets.text("modified_before", "", "modified_before")

# base load parameters
dbutils.widgets.text("hold_file_if_schema_failed", "true", "hold_file_if_schema_failed")
dbutils.widgets.text("base_merge_schema", "true", "stage_merge_schema")

# COMMAND ----------

from etl import get_table, BaseTable
import logging
from datetime import datetime

process_id:int = int(dbutils.widgets.get("process_id"))
table:str = dbutils.widgets.get("table")
load_type:str = dbutils.widgets.get("load_type")
force:bool = (dbutils.widgets.get("force") == "true")
stage_merge_schema:bool = (dbutils.widgets.get("stage_merge_schema") == "true")
# if true the entire file will be held at stage if it has schema errors.
hold_file_if_schema_failed:bool = (dbutils.widgets.get("hold_file_if_schema_failed") == "true")
base_merge_schema:bool = (dbutils.widgets.get("base_merge_schema") == "true")

modified_after = dbutils.widgets.get("modified_after")
modified_after = datetime.strptime(modified_after, "%Y-%m-%d %H:%M:%S") if modified_after else None

modified_before = dbutils.widgets.get("modified_before")
modified_before = datetime.strptime(modified_before, "%Y-%m-%d %H:%M:%S") if modified_before else None

table = get_table(spark = spark, table = table, load_type = load_type)
logger = logging.getLogger(f"load_table(table = {table.name}, load_type = {load_type}), process_id = {process_id}")

# COMMAND ----------


catalog = f"{table.environment}_hub"
spark.sql(f"use catalog {catalog}")
logger.info(f"default catalog set to {catalog}")

# COMMAND ----------

table.stage_into(
    process_id = process_id, 
    merge_schema = stage_merge_schema, 
    force = force,
    modified_after = modified_after,
    modified_before = modified_before
)

# COMMAND ----------

df = table.load_audit(process_id = process_id)
if df:
  display(df)

# COMMAND ----------

df = table.extract(
  process_id=process_id, 
  hold_file_if_schema_failed=hold_file_if_schema_failed
)

# COMMAND ----------

df = table.transform(df=df)

# COMMAND ----------

df = table.load(df=df)
display(df)

# COMMAND ----------

dbutils.notebook.exit(f"load_table {catalog}.{table.db}.{table.name} succeeded with process_id = {process_id}")

# COMMAND ----------


# from etl.utils import convert_schema, FileTypes

# convert_schema("../schema/")
