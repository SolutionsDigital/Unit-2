from bottle import Bottle, request, template
import bottle_sqlite
import sqlite3

app=Bottle()
path_to_templates = ["./views"]

def create_tables(db):
    """create tables for the web app"""
    cursor = db.cursor()
    # delete the likes table if it exists (this is for testing only)
    cursor.execute("DROP TABLE IF EXISTS likes")
    # create a new clean likes table
    cursor.execute("CREATE TABLE likes (thing text)")

def store_likes(db, like):
    """store a like in a db"""
    cursor = db.cursor()
    # using ? as a positional placeholder. The second argument of cursor.execute() needs to be a list
    cursor.execute("INSERT INTO likes (thing) VALUES (?)", [like])


def get_likes(db):
    """how to retrieve data and return a list of likes"""
    cursor = db.cursor()
    cursor.execute("SELECT thing from likes")
    result = []
    # No cursor.fetchall()???
    for row in cursor:
        result.append(row['thing'])
    return result

@app.route("/", method="GET")
def serve_form():
    return template("likes_form.tpl", template_lookup=path_to_templates)

@app.route("/", method="POST")
def index(db):
    """Home Page"""
    info = {
        "title":"Welcome home",
        "likes":get_likes(db)
    }

    return template("dblikes.tpl", info, template_lookup=path_to_templates)

@app.route("/likes", method="POST")
def like(db):
    """Process like form request"""
    likes = request.forms.get("likes")

    # If there is a value in the like field
    if likes:
        # store it in the db
        store_likes(db, likes)

    # query the db for a return page
    info = {
        "title":"Welcome home",
        "likes":get_likes(db)
    }
    # display a return page
    return template("dblikes.tpl", info, template_lookup=path_to_templates)

if __name__=="__main__":
    DATABASE_NAME = "test.db"
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)

    """The database plugin is used to manage the connection and route handlers"""
    plugin=bottle_sqlite.Plugin(dbfile=DATABASE_NAME)
    app.install(plugin)

    app.run(debug=True)
