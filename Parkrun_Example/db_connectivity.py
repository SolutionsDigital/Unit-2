import bottle, bottle_sqlite, sqlite3

app=bottle.Bottle()
# plugin=bottle_sqlite.Plugin(dbfile="parkrun_db.db")
# app.install(plugin)

# @app.route("/show/:item")
# def show(item, db):
#     cursor = db.cursor()
#     cursor.execute("SELECT TeamName FROM Teams WHERE TeamName=?", item)
#     row = cursor.fetchone()
#     if row:
#         return str(row)


def create_table(db):
    """Create database table for the likes application
    given a database connection 'db'.
    Removes any existing data that might be in the
    database."""

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS likes")
    cursor.execute("""
    CREATE TABLE likes (
       thing text
    )
    """)

def store_like(db, like):
    """Store a new like in the database"""

    cursor = db.cursor()
    cursor.execute("INSERT INTO likes (thing) VALUES (?)", [like])
    db.commit()

def get_likes(db):
   """Return a list of likes from the database"""

   cursor = db.cursor()
   cursor.execute("SELECT thing FROM likes")
   result = []
   for row in cursor:
       result.append(row['thing'])
   return result

def get_likes(db):
   """Return a list of likes from the database"""

   cursor = db.cursor()
   cursor.execute("SELECT thing FROM likes")
   result = []
   for row in cursor:
       result.append(row['thing'])
   return result

@app.post('/likes')
def like(db):
    """Process like form post request"""

    # get the form field
    likes = request.forms.get('likes')

    if likes:
        store_like(db, likes)

    return redirect('/')

if __name__ == "__main__":
    # code to connect to the database and create the tables
    DATABASE_NAME = 'test.db'
    db = sqlite3.connect("thingy.db")
    create_table(db)

    # code to run our web application
    plugin = bottle_sqlite.Plugin(dbfile="thingy.db")
    app.install(plugin)

    # run the application
    app.run()

if __name__=="__main__":
    app.run(debug=True)
