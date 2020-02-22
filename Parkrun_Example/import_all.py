import sqlite3
import csv

db_filename = "parkrun_db.db"

#All Bindings must be provided with a value in the csv use "None" if data is not available
#The PK is AI in the DB Table
data_filename = "./CSVs/all_results.csv"

sql_statement ="""
INSERT INTO All_Results (ParkRunner, Time, Gender, Club, EventID)
VALUES (:ParkRunner, :Time, :Gender, :Club, :EventID)
"""

print(sql_statement)

# Open the source file in "with" statement
with open(data_filename,'rt') as csv_file:
    #create a DictReader (part of csv library) object
    csv_reader = csv.DictReader(csv_file)
    print(csv_reader)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        #executemany() will execute until EOF of csv_reader
        #second paramter of the executemany() instantiates the named parameters
        cursor.executemany(sql_statement,csv_reader)
