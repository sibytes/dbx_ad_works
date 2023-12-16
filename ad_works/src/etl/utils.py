import os
import logging
from pyspark.sql import SparkSession
from enum import Enum
import jinja2
from typing import Dict

class Variables(Enum):
    DATABASE = "database"
    TABLE = "table"
    PROJECT = "project"
    CATALOG = "catalog"
    COLUMNS = "columns"

def render_jinja(
  data: str, 
  replacements:Dict[Variables, str]
):
  logger = logging.getLogger(__name__)
  logger.debug(f"Rendering Jinja string {data}")
  if data and isinstance(data, str):
      replace = {k.value: v for (k, v) in replacements.items()}
      skip = False
      for k, v in replace.items():
          if v is None and "{{" + k + "}}" in data.replace(" ", ""):
              skip = True
              break

      if not skip:
          template: jinja2.Template = jinja2.Template(data)
          data = template.render(replace)
  logger.debug(f"Rendered Jinja string {data}")

  return data
  
def load_sql(
  name:str, 
  root:str="./../sql", 
  variables: Dict[Variables, str] | None = None
):
  logger = logging.getLogger(__name__)
  path = os.path.join(os.getcwd(), root, f"{name}.sql")
  logger.info(f"loading sql {path}")

  with open(path, "r", encoding="utf-8") as f:
    sql = f.read()

  if isinstance(variables, dict):
    sql = render_jinja(sql, variables)
  
  return sql

def get_environment(spark:SparkSession):

  logger = logging.getLogger(__name__)
  envs = {
     "adb-8723178682651460": "dev",
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



  
