import sqlite3


#create a connection (a connection object) the db
myConn = sqlite3.connect("parkrun_db.db")


"""
create a cursor for all distinct runners
create a list of tuples each tuple is a record in Runners the table
each tuple item is a value in one of the fields of the table
[(1, 'Aaron COSGROVE', 'M'), (2, 'Aaron HALL', 'M'), ...]
"""
ListOfDistinctRunners = myConn.cursor()
ListOfDistinctRunners.execute("SELECT * FROM Runners")
Runners = ListOfDistinctRunners.fetchall()


"""
create a second cursor for all results
create a list of tuples each tuple is a record in the Results table
each tuple item is a value in one of the fields of the table
[('Aaron COSGROVE', '36:37:00', 'M', None, 6), ('Aaron COSGROVE', '29:34:00', 'M', None, 12),
('Aaron COSGROVE', '26:39:00', 'M', None, 11), ('Aaron COSGROVE', '27:17:00', 'M', None, 10),
('Aaron HALL', '38:25:00', 'M', None, 4), ('Aaron HANNAH', '23:41', 'M', None, 14),
('Aaron HANNAH', '19:20', 'M', None, 13),...
"""
ListOfAllResults = myConn.cursor()
ListOfAllResults.execute("SELECT * FROM All_Results")
Results = ListOfAllResults.fetchall()


#Iterating over the Runners list of tuples
for runner in Runners:
    for result in Results:
        #Matching a runner and their results
        if runner[2] == result[0]:
            #print(the runner's ID, their result and the event ID)
            print(str(runner[0])+","+str(result[1])+","+str(result[4]))
            query = "INSERT INTO Results (RunnerID, Time, EventID) VALUES (?,?,?)"
            values = (str(runner[0]),str(result[1]),str(result[4]))
            ListOfDistinctRunners.execute(query,values)

myConn.commit()

