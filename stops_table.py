from pyspark.sql import SparkSession
from cassandra_config import cassandra_options

options = cassandra_options
options["keyspace"] = "ctp_data"
options["table"] = "stops"

spark = SparkSession.builder.appName("Cassandra-AWS") \
    .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.4.1") \
    .config("spark.cassandra.connection.ssl.enabled", "true") \
    .config("spark.cassandra.connection.ssl.trustStore.type", "CRT") \
    .getOrCreate()

stops_dataframe_reader = spark.read \
    .format("org.apache.spark.sql.cassandra") \
    .options(**options) \
    # .load()

# df.show(100, truncate=False)
