#import the sqlite3 module
import sqlite3

#create a connection (a connection object) to a non existing db creates that db
myConn = sqlite3.connect ("parkun_db.db")