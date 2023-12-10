from abc import ABC, abstractmethod
from pyspark.sql import DataFrame, SparkSession
import logging
from typing import Optional
from datetime import datetime
from .utils import load_sql, get_environment

class BaseTable(ABC):

  _SCHEMA_PATH = "./../schema"
  _SQL_PATH = "./../sql"

  def __init__(
      self,
      spark:SparkSession,
      name:str,
      filename:str,
      primary_keys:list
      ):
    self._logger = logging.getLogger(self.__class__.__name__)

    self.spark = spark
    # custom table properties
    self.name = name
    self.filename = filename
    self.primary_keys = primary_keys
    self.environment = get_environment(spark = self.spark)
    self.raw_db = "raw_fnz_pb"
    self.db = "fnz_pb"
    
  def _get_merge_on_clause(self):
    sql = [ f"src.{k} = dst.{k}" for k in self.primary_keys]
    sql = " and ".join(sql)
    return sql

  def _load_sql(self, name:str):
    sql = load_sql(name, self._SQL_PATH)    
    return sql
  
  @abstractmethod
  def stage_into(
      self, 
      process_id:int, 
      merge_schema=True, 
      force=False,
      modified_after:Optional[datetime] = None,
      modified_before:Optional[datetime] = None
  ):
    pass

  @abstractmethod
  def load_header_footer(
    self, 
    process_id: int
  ) -> Optional[DataFrame]:
    pass

  @abstractmethod
  def extract(
    self,
    process_id:int,
    hold_file_if_schema_failed:bool = True
  ) -> DataFrame:
    pass

  @abstractmethod
  def transform(
    self, 
    df:DataFrame
  ) -> DataFrame:
    pass

  @abstractmethod
  def load(
    self,
    df:DataFrame
  ) -> DataFrame:
    pass
