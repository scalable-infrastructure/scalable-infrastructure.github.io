# Terasort

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar teragen 10000000 teragen
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar terasort teragen teraout


# Streaming

cat /data/NASA_access_log_Jul95 | awk  '{print $(NF-1)}'| 	sort | uniq -c



head /data/NASA_access_log_Jul95 |python map_reduce.py map | sort | python map_reduce.py reduce

cat /data/NASA_access_log_Jul95 |python map_reduce.py map | sort | python map_reduce.py reduce


hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -files map_reduce.py -input input-nasa/ -output output-nasa/   -mapper 'map_reduce.py map' -reducer 'map_reduce.py reduce'


##########################################################
>>> l = [1,2,3,4]

>>> map(lambda x:x,  l)
[1, 2, 3, 4]
>>> map(lambda x: x**2,  l)
[1, 4, 9, 16]
>>> reduce(lambda x,y: x+y,  l)


# Word count
text_rdd = sc.textFile("hdfs://ip-10-186-164-81:8022/user/luckow/input/")
text_rdd.collect()
text_rdd.count()

text_rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x,y: x+y).collect()

# NASA
text_rdd = sc.textFile("hdfs://ip-10-186-164-81:8022/user/luckow/input-nasa/")
text_rdd.filter(lambda x: len(x)>8).map(lambda x: (x.split()[-2],1)).reduceByKey(lambda x,y: x+y).collect()


################################################################
#
from pyspark.sql import SQLContext, Row
sqlContext = SQLContext(sc)


text_filtered = text_rdd.filter(lambda x: len(x)>8)
logs = text_filtered.top(20)

cleaned = text_filtered.map(lambda l: (l.split(" ")[0], l.split(" ")[3][1:], l.split(" ")[6], l.split(" ")[-2]))

rows = cleaned.map(lambda l: Row(referer=l[0], ts=l[1]))

schemaLog = sqlContext.inferSchema(rows)
schemaLog.registerTempTable("row")




