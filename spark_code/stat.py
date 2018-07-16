from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df_sleep = spark.read.json("../data/2/sokulee/*/*_sleep.json")
df_steps = spark.read.json("../data/2/sokulee/*/*_steps.json")

df_sleep.printSchema()

sleep_total_minutes_sleep = df_sleep.select(df_sleep['summary']['totalMinutesAsleep'])
sleep_total_time_in_bed = df_sleep.select(df_sleep['summary']['totalTimeInBed'])

print(sleep_total_minutes_sleep.show())
df_sleep.select(F.mean(df_sleep['summary']['totalMinutesAsleep']), F.min(df_sleep['summary']['totalMinutesAsleep']), F.max(df_sleep['summary']['totalMinutesAsleep'])).show()
