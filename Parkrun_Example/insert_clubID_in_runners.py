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

"""
create a third cursor for the RunningClubs
"""

ListOfDistinctClubs = myConn.cursor()
# ListOfDistinctClubs.execute("SELECT * FROM Clubs")
# Clubs = ListOfDistinctClubs.fetchall()

#Iterating over the Runners list of tuples
for runner in Runners:
    for result in Results:
        #Matching a runner, their results and their potential club
        if runner[2] == result[0] and result[3]:
            #search for the ID of the club the runner is associated with
            ListOfDistinctClubs.execute("SELECT * FROM Clubs WHERE CLubName LIKE \"" + str(result[3])+"\"")
            Clubs = ListOfDistinctClubs.fetchone()
            # Write the ClubID to the runners' record in the Runners table
            # i.e. Update the RunningClubID of the RunnerID the cursor is at
            query = "UPDATE Runners Set RunningClubID = ? WHERE RunnerID = ?"
            values = (str(Clubs[0]),str(runner[0]))
            ListOfDistinctRunners.execute(query,values)

myConn.commit()

