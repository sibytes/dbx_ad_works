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

from etl import tables
dependencies_list = [f"""        - task_key: {table}
          depends_on:
            - task_key: initialise
          notebook_task:
            notebook_path: /Repos/shaun.ryan@shaunchiburihotmail.onmicrosoft.com/dbx_ad_works/ad_works/src/load_table
            base_parameters:
              table: ""
            source: WORKSPACE
          existing_cluster_id: 1003-160019-i21cm8l3"""
   for table, details in tables().items()]

with open("./scratch.txt", "w") as f:
  f.write("\n".join(dependencies_list))

# COMMAND ----------

dbutils.fs.rm("/Volumes/dev_hub/checkpoints/ad_works/stage_ad_works_person_business_entity_address", True)

# COMMAND ----------


# from etl.utils import convert_schema, FileTypes

# convert_schema("../schema/")
