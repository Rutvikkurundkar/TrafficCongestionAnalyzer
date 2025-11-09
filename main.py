from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import matplotlib.pyplot as plt
import os

# Creating a Spark session
spark = SparkSession.builder.appName("TrafficCongestionAnalyzer").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Lode Dataset
data_path = "data/metro.csv"  

df = spark.read.csv(data_path, header=True, inferSchema=True)
print("\n Dataset Loaded Successfully\n")
df.show(10)

# 3. PARSE TIMESTAMP + CREATE NEW COLUMNS

df = df.withColumn("timestamp", to_timestamp("date_time", "M/d/yyyy H:mm"))

# Extract hour, day of week, month
df = df.withColumn("hour", hour("timestamp"))
df = df.withColumn("day", date_format("timestamp", "E"))
df = df.withColumn("month", month("timestamp"))


# Hourly Traffic Analysis

hourly = df.groupBy("hour") \
           .agg(avg("traffic_volume").alias("avg_volume")) \
           .orderBy("hour")

hourly_pd = hourly.toPandas()

os.makedirs("outputs/figures", exist_ok=True)

plt.figure(figsize=(10,5))
plt.plot(hourly_pd["hour"], hourly_pd["avg_volume"], marker='o')
plt.title("Hourly Traffic Volume Trend")
plt.xlabel("Hour (0–23)")
plt.ylabel("Average Traffic Volume")
plt.grid(True)
plt.savefig("outputs/figures/hourly_trend.png")
plt.close()
print(" Saved: outputs/figures/hourly_trend.png")

# Day of week analysis

daily = df.groupBy("day") \
          .agg(avg("traffic_volume").alias("avg_volume"))

daily_pd = daily.toPandas()

plt.figure(figsize=(10,5))
plt.bar(daily_pd["day"], daily_pd["avg_volume"], color='skyblue')
plt.title("Day of Week Traffic Volume")
plt.xlabel("Day")
plt.ylabel("Average Traffic Volume")
plt.savefig("outputs/figures/daywise_trend.png")
plt.close()
print(" Saved: outputs/figures/daywise_trend.png")


# Monthly Traffic Trend

monthly = df.groupBy("month") \
            .agg(avg("traffic_volume").alias("avg_volume")) \
            .orderBy("month")

monthly_pd = monthly.toPandas()

plt.figure(figsize=(10,5))
plt.plot(monthly_pd["month"], monthly_pd["avg_volume"], marker='o', color='green')
plt.title("Monthly Traffic Volume Trend")
plt.xlabel("Month")
plt.ylabel("Average Traffic Volume")
plt.grid(True)
plt.savefig("outputs/figures/monthly_trend.png")
plt.close()
print(" Saved: outputs/figures/monthly_trend.png")


print("Check the 'outputs/figures/' folder for charts.\n")

