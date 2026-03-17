# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "14bc786b-5d60-4afd-a4ea-487d8199e166",
# META       "default_lakehouse_name": "FUAM_Lakehouse",
# META       "default_lakehouse_workspace_id": "ee115055-0f6f-4b77-a7d2-df160569fa58"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Lakehouse Optimization
# This notebook uses optimize and vacuum for the lakehouse tables in order to delete unnecessary historic files and optimize performance

# PARAMETERS CELL ********************

number_of_days = 7 # must be bigger than 7 days, otherwise setting must be changed, this is used for vaccuum

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql 
# MAGIC SET spark.sql.parquet.vorder.enabled

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

tables = spark.catalog.listTables()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

for tab in tables:
    print(tab.name)

    print("Run Optimize")
    spark.sql("""
        OPTIMIZE FUAM_Lakehouse.""" + tab.name + """ VORDER;
    """)

    print("Run Vacuum")
    spark.sql("""
        VACUUM FUAM_Lakehouse.""" + tab.name + """ RETAIN """ + str(number_of_days * 24) + """ HOURS
    """)

    


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
