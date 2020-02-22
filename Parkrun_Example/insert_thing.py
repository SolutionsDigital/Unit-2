import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()
sqlstatement = "INSERT INTO likes (thing) VALUES (?)"
pos_param = ("coffee",)

cursor.execute(sqlstatement, pos_param )
db.commit()


