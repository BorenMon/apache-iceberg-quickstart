# from minio import Minio
# import pandas as pd  # type: ignore
# from io import BytesIO
from pyspark.sql import SparkSession


spark: SparkSession = SparkSession
spark = spark.builder.remote("sc://localhost:15002").getOrCreate()

# # Initialize the MinIO client
# minio_client = Minio(
#     endpoint='localhost:9000',
#     access_key='admin',
#     secret_key='password',
#     secure=False
# )

# # Define the bucket name and file path in the bucket
# bucket_name = "temp"
# object_name = "random_data.csv"

# try:
#     # Step 1: Fetch the CSV file from MinIO as a stream
#     response = minio_client.get_object(bucket_name, object_name)

#     # Step 2: Read the CSV content directly into a pandas DataFrame
#     df_pandas = pd.read_csv(BytesIO(response.read()))

#     # Step 3: Convert the pandas DataFrame to a list of tuples
#     data = list(df_pandas.itertuples(index=False, name=None))

#     # Step 4: Fetch the schema from the Iceberg table
#     schema = spark.table("demo.nyc.taxis").schema

#     # Step 5: Create a Spark DataFrame with the schema of the Iceberg table
#     df_spark = spark.createDataFrame(data, schema)

#     # Step 6: Append the Spark DataFrame to the Iceberg table
#     df_spark.writeTo("demo.nyc.taxis").append()

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # Close the response to avoid resource leaks
#     if 'response' in locals() and response:
#         response.close()

# # Stop the Spark session after job completion
# spark.stop()

# List all namespaces (databases) in the 'my_catalog'
namespaces = spark.sql("SHOW NAMESPACES IN demo")
namespaces.show()