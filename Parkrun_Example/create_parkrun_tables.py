import sqlite3

#create a connection (a connection object) the db
myConn = sqlite3.connect("parkrun_db.db")

# create a cursor
myCursor = myConn.cursor()

SQLStatement = ""

#list the fields in a dictionary. the key is the field name
#the value is the list of parameters for that field
Chaptersfields =	{
    "ChapterID":"INTEGER PRIMARY KEY AUTOINCREMENT",
    "ChapterName":"TEXT NOT NULL",
    "ChapterAddress":"TEXT NOT NULL",
    "ChapterPhoto":"TEXT",
    "ChapterEmail":"TEXT NOT NULL",
    "CourseMap":"TEXT",
    "CourseDescription":"BLOB",
    "Facilities":"BLOB",
    "LocationOfStart":"TEXT NOT NULL",
    "GettingTherePublicTransport":"BLOB",
    "GettingThereFoot":"BLOB",
    "GettingThereRoad":"BLOB"
    }

Runnersfields = {
  "RunnerID": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "RegistrationDate": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
    "FirstName": "TEXT",
    "LastName": "TEXT",
    "HomeRun": "INTEGER",
    "Gender": "INTEGER",
    "RunningClubID": "INTEGER",
    "Email": "TEXT",
    "Postcode": "TEXT",
    "SignUpToEmails": "INTEGER DEFAULT 1",
    "RecentExerciseFrequency": "INTEGER",
    "MedicalCondition": "BLOB",
    "EmergencyContactName": "TEXT",
    "EmergencyContactNumber": "TEXT"
  }

Clubsfields = {
    "RunningClubID":"INTEGER PRIMARY KEY AUTOINCREMENT",
    "RunningCLubName":"TEXT NOT NULL"
    }

Recentexercisefrequencyfields = {
    "RecentExerciseFrequencyID":"INTEGER PRIMARY KEY AUTOINCREMENT",
    "RecentExerciseDescription":"TEXT NOT NULL"
    }

Eventsfields={
    "EventID":"INTEGER PRIMARY KEY AUTOINCREMENT",
    "EventDate":"TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
    "RunnerID":"INTEGER NOT NULL",
    "RunnerTime":"INTEGER NOT NULL",
    "ChapterID":"INTEGER NOT NULL"
    }

Resultsfields={
    "ResultID":"INTEGER PRIMARY KEY AUTOINCREMENT",
    "RunnerID":"INTEGER",
    "Time":"TEXT",
    "EventID":"INTEGER"
}

sql_statement = "CREATE TABLE \""
#Start building the SQL statement with the name of the table
def createTable(tablename, fields):
    sql_statement = "CREATE TABLE \""
    sql_statement += tablename + "\" ("

    for x in fields:
        sql_statement += "\""+x+"\" "+fields[x]+","
        #Trim the trailing "'" and add a closing parenthesis
    return sql_statement[:-1]+")"


#Execute the SQL Statement
# myCursor.execute(createTable("Chapters",Chaptersfields))
# myCursor.execute(createTable("Runners",Runnersfields))
# myCursor.execute(createTable("Events",Eventsfields))
# myCursor.execute(createTable("Clubs",Clubsfields))
# myCursor.execute(createTable("RecentExerciseFrequency",Recentexercisefrequencyfields))
myCursor.execute(createTable("Results",Resultsfields))

