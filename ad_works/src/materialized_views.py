# Databricks notebook source
df = spark.sql("
select round(sum(line_total), 4) as total, cast(modified_date as date) as date
from ad_works.sales_sales_order_detail
group by all
order by date desc
")

display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create schema if not exists dev_hub.ad_works_dw;
# MAGIC use catalog dev_hub;
# MAGIC use schema ad_works_dw;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE MATERIALIZED VIEW if not exists sales
# MAGIC AS 
# MAGIC
# MAGIC select round(sum(line_total), 4) as total, cast(modified_date as date) as date
# MAGIC from ad_works.sales_sales_order_detail
# MAGIC group by all
# MAGIC order by date desc
# MAGIC
