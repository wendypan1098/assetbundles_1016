import dlt
@dlt.table
def transformaed():
   return spark.range(10)