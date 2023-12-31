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
import yaml

task = {
  "task_key": "",
  "depends_on": [
  ],
  "notebook_task" : None,
  "existing_cluster_id": "1003-160019-i21cm8l3"
}
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

tasks = []
prev_table = "initialise"
i = 0
for table, details in tables().items():
  this_task = task.copy()
  this_task["task_key"] = table
  this_task["depends_on"] = [{"task_key": prev_table}]
  this_task["notebook_task"] = {
    "notebook_path": "/Repos/shaun.ryan@shaunchiburihotmail.onmicrosoft.com/dbx_ad_works/ad_works/src/load_table",
    "base_parameters": {
      "table": table
    },
    "source": "WORKSPACE"
  }
  tasks.append(this_task)

  if i == 16:
    prev_table = "initialise"
    i = 0
  else:
    prev_table = table
    i += 1


tasks = {"tasks": tasks}

with open("../scratch/scratch.yaml", "w") as f:
  f.write(yaml.dump(tasks, indent=4, Dumper=NoAliasDumper))


# COMMAND ----------


checkpoints = {p.path: dbutils.fs.rm(p.path, True) for p in dbutils.fs.ls("/Volumes/dev_hub/checkpoints/ad_works")}
checkpoints

# COMMAND ----------


# from etl.utils import convert_schema, FileTypes

# convert_schema("../schema/")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from dev_hub.ad_works.`_audit`

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from dev_hub.stage_ad_works.sales_currency_rate
