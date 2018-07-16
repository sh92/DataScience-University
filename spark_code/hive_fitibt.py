import os
from os.path import expanduser, join
from pyspark.sql import SparkSession
from pyspark.sql import Row

warehouse_location = os.path.dirname( os.path.abspath( __file__) ) + '/spark-warehouse'

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Python Spark SQL Hive integrationn example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("create table tashu (RENT_STATION int, RENT_DATE string, RETURN_STATION int, RETURN_DATE string) row format delimited fields terminated by ',' TBLPROPERTIES ('skip.header.line.count'='1')")
filePath = "/root/data/2/sokulee/*/*_steps.json")

spark.sql("load data local inpath '"+filePath+"' overwrite into table tashu")
spark.sql("select word, count(*) as cnt from tashu LATERAL VIEW explode(split(substr(rent_date, 1, 4), ' ')) lTable as word where cast(word as int) is not null group by word order by cnt desc").show()
result = spark.sql("select cast(word as int), count(*) as cnt from tashu LATERAL VIEW explode(split(substr(rent_date,7,2), ' ')) lTable as word where cast(word as int) is not null group by word order by cnt desc")
result.show()
top10_station = spark.sql("select word, count(*) as cnt from tashu LATERAL VIEW explode(split(RENT_STATION, ' ')) lTable as word group by word order by cnt desc limit 10")
top10_station.show()

outfilepath= "top10.txt"
top10_station.rdd.map(lambda r: ",".join([str(c) for c in r])).saveAsTextFile(outfilepath)

spark.sql("drop table tashu")
