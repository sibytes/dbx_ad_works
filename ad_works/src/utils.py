# Databricks notebook source
# MAGIC %md
# MAGIC # Main Entry Point for a Table Load Task
# MAGIC
# MAGIC This default notebook is executed using Databricks Workflows as defined in resources/ingest_ad_works_job.yml.

# COMMAND ----------

# MAGIC %pip install pyyaml
# MAGIC

# COMMAND ----------

from etl import tables

dependencies_list = [f"            - task_key: {table}" for table, details in tables().items()]

with open("./scratch.txt", "w") as f:
  f.write("\n".join(dependencies_list))



# COMMAND ----------


# from etl.utils import convert_schema, FileTypes

# convert_schema("../schema/")
