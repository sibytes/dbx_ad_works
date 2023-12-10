import os
import logging
from pyspark.sql import SparkSession


def load_sql(name:str, root:str="./../sql"):
  logger = logging.getLogger(__name__)
  path = os.path.join(os.getcwd(), root, f"{name}.sql")
  logger.info(f"loading sql {path}")

  with open(path, "r", encoding="utf-8") as f:
    sql = f.read()
  
  return sql

def get_environment(spark:SparkSession):

  logger = logging.getLogger(__name__)
  envs = {
     "adb-8723178682651460.0": "dev",
     "?": "tst",
     "?": "pre",
     "?": "prd"
  }
  workspace = spark.conf.get("spark.databricks.workspaceUrl").split(".")[0]
  logger.debug(f"Detected the workspace {workspace} for environment configuration")
  try:
    env = envs[workspace]
  except KeyError as e:
    msg = f"Workspace {e} not found in environment configuration"
    logger.error(msg)
    raise Exception(msg)

  if env not in ("dev", "tst", "pre", "prd"):
      msg = f"unknown QDP environment name {env}"
      logger.error(msg)
      raise Exception(f"unknown QDP environment name {env}")
  
  logger.info(f"Detected the {env} environment")

  return env