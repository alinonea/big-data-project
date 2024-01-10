from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
cassandra_jar = './spark-cassandra-connector_2.13-3.4.1.jar'

spark = SparkSession.builder.appName("Cassandra-AWS") \
    .config("spark.jars", cassandra_jar) \
    .config("spark.cassandra.connection.host", "cassandra.eu-north-1.amazonaws.com") \
    .config("spark.cassandra.connection.port", "9142") \
    .config("spark.cassandra.auth.username", "nodejs-script-at-211125392861") \
    .config("spark.cassandra.auth.password", "Ewy3qUp6abAeoEUdQg10CEx/5PJ+Z53eQTT77pjv1og=") \
    .getOrCreate()

df = spark.read \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "ctp_data") \
    .option("table", "vehicles") \
    .load()

df.show()