from bottle import Bottle, template, request
import bottle_sqlite
import sqlite3

app = Bottle()

def get_clubs(db):
    """how to retrieve data and return a list of likes"""
    cursor = db.cursor()
    cursor.execute("SELECT ClubID, ClubName from Clubs ORDER BY ClubName")
    result = []
    for row in cursor:
        ClubandID = []
        # Collect the name and the id in a list
        ClubandID.append(row['ClubName'])
        ClubandID.append(row['ClubID'])
        #append the list above tho the result list (a list of lists)
        result.append(ClubandID)
    return result


@app.route("/", method="GET")
def loop(db):
    #CReate a dictionary to pass to the template function
    # the value corresponding to the ClubNames key is "results" (a list of lists)
    clubs = {
        "ClubNames": get_clubs(db)
        }
    return template("drop_down_list.tpl", clubs, template_lookup=["./views"])

@app.route("/", method="POST")
def return_choice():
    # recover the value of the item selected in the dropdown
    name = request.forms.get("Club")
    return "the ClubID of the club you selected is " + str(name)

if __name__ == '__main__':

    DATABASE_NAME = "parkrun_db.db"
    db = sqlite3.connect(DATABASE_NAME)

    """The database plugin is used to manage the connection and route handlers"""
    plugin=bottle_sqlite.Plugin(dbfile=DATABASE_NAME)
    app.install(plugin)
    app.run(debug=True)
