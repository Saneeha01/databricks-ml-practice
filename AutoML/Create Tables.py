# Databricks notebook source
# MAGIC %md
# MAGIC ## Creating Tables for Regression

# COMMAND ----------

from pyspark.sql.types import DoubleType, StringType, StructType, StructField
 
schema = StructType([
  StructField("longitude", DoubleType(), True),
  StructField("latitude", DoubleType(), True),
  StructField("housing_median_age", DoubleType(), True),
  StructField("total_rooms", DoubleType(), True),
  StructField("total_bedrooms", DoubleType(), True),
  StructField("population", DoubleType(), True),
  StructField("households", DoubleType(), True),
  StructField("median_income", DoubleType(), True),
  StructField("median_house_value", DoubleType(), True),
  StructField("ocean_proximity", StringType(), True)
])
 
housing_df = spark.read.format("csv").schema(schema).option("header", "true").load("/FileStore/housing.csv")
