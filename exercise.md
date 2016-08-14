---
layout: page
title: "In-Class Exercises"
description: ""
---
{% include JB/setup %}



# Infrastructure

* Linux Cluster hosted at Amazon EC2
* Cloudera Cluster (CDH 5.1) running on Ubuntu 12.04
* Access via SSH (Windows User can use [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html))
* Python 2.7.3, Python Documentation: <http://docs.python.org/>
* Hostname: `cloud.luckow-hm.de (54.83.41.227)`
* HDFS Web: <http://cloud.luckow-hm.de:50070/>
* YARN Web: <http://cloud.luckow-hm.de:8088/cluster>
* Cloudera Manager: <http://cloud.luckow-hm.de:7180/>

***Please change your initial password with `passwd`!***

<br/>

# 1. Using SSH and Linux
<br/>
***Data/Tools***:

* Use an SSH client of your choice (e.g. Putty for Windows or SSH in your Linux/Mac OS Terminal)
* Data: `cloud.luckow-hm.de:/data/NASA_access_log_Jul95`


1. Please login into the Hadoop cluster on Amazon!

1. Answer the following questions using the command (`hadoop dfsadmin -report`):
    * How big is the Hadoop cluster?
    * How many data nodes are used?

1. Upload the file `cloud.luckow-hm.de:/data/NASA_access_log_Jul95` to your HDFS home directory! How many blocks does HDFS allocate for this file? On what host are these blocks?

<br/>

# 2. MapReduce Hello World

<br/>

***Data/Tools***:

* MapReduce Application: `hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount`

Run the WordCount example of Hadoop:

1. Create two test files containing text and upload them to HDFS!
1. Use the MapReduce program WordCount for processing these files!

<br/>

# 3. Commandline Data Analytics

<br/>  

***Data/Tools***:

* <http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html>
* Commandline data tools <https://github.com/bitly/data_hacks>
* Data: `cloud.luckow-hm.de:/data/NASA_access_log_Jul95`

<br/>

1. Use the commands `head`, `cat`, `uniq`, `wc`, `sort`, `find`, `xargs`, `awk` to evaluate the NASA log file:

    * Which page was called the most?
    * What was the most frequent return code?
    * How many errors occurred? What is the percentage of errors?


2. Implement a Python version of this Unix Shell script using this [script](src/map_reduce.py) as template!


3. Run the Python script inside an Hadoop Streaming job.

        hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -info

<br/>



# 4. Spark
<br/>  
***Data/Tools***:

* Spark Programming Guide: <https://spark.apache.org/docs/1.1.0/programming-guide.html> (use Python API recommended)
* Spark API: <https://spark.apache.org/docs/1.1.0/api/python/index.html>

1. Implement a wordcount using Spark. Make sure that you only allocate 1 core for the interactive Spark shell:

        pyspark --total-executor-cores 1


2. Implement the NASA log file analysis using Spark!

[Solution](src/spark.py)

<br/>  

# 5. Hadoop SQL Engines
<br/>  
***Data/Tools***:

* Hive User Guide: <https://cwiki.apache.org/confluence/display/Hive/GettingStarted>
* Hive ORC: <http://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.0.0.2/ds_Hive/orcfile.html>
* Hive Parquet: <http://www.cloudera.com/content/cloudera/en/documentation/cdh5/v5-0-0/CDH5-Installation-Guide/cdh5ig_parquet.html>


1. Create a Hive table for the NASA Log files! Use either `python` or `awk` to convert the log file to a structured format (CSV) that is manageable by Hive! Use the text format for the table definition!

        cat /data/NASA_access_log_Jul95 |awk -F' ' '{print "\""$4 $5"\","$(NF-1)","$(NF)}' > nasa.csv

2. Run an SQL query that outputs the number of occurrences of each HTTP response code!

3. Based on the initially created table define an ORC and Parquet-based table. Repeat the query!

4. Run the same query with Impala!

[Solution](src/sql-hive-solution.txt)
<br/>  

# 6. Data Analytics
<br/>
***Data/Tools***:

* Spark MLLib KMeans Example: <https://spark.apache.org/docs/1.1.0/mllib-clustering.html>


1. Run KMeans on the provided example [dataset](src/kmeans/kmeans_data.txt)!

2. Validate the quality of the model using the sum of the squared error for each point!

[Solution](src/sql-hive-solution.txt)
<br/>

# 7. Hadoop Benchmarking
<br/>  

1. Run the program `Terasort` on 1 GB of data - each record that TeraGen generates is 100 Bytes in size:

        hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar teragen <number_of_records> <output_directory>

        hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar terasort <input_directory> <output_directory>

1. How many containers are consumed during which phase of the application: teragen, terasort (map phase, reduce phase)? Please explain! See [blog post](http://blog.cloudera.com/blog/2014/04/apache-hadoop-yarn-avoiding-6-time-consuming-gotchas/).

<br/>  
