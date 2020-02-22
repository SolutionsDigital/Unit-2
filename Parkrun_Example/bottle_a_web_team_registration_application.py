from bottle import Bottle, request, template
import bottle_sqlite
import sqlite3

app = Bottle()
path_to_templates = ["./views"]


def store_team_name(db, teams):
    """store a like in a db"""
    cursor = db.cursor()
    # using ? as a positional placeholder. The second argument of cursor.execute() needs to be a list
    cursor.execute("INSERT INTO Teams (TeamName) VALUES (?)", [teams])


def get_teams(db):
    """how to retrieve data and return a list of teams"""
    cursor = db.cursor()
    cursor.execute("SELECT TeamID, TeamName from Teams ORDER BY TeamName")

    result = []
    for row in cursor:
        TeamAndID = []
        # Collect the name and the id in a list
        TeamAndID.append(row['TeamID'])
        TeamAndID.append(row['TeamName'])
        # append the list above tho the result list (a list of lists)
        result.append(TeamAndID)
    return result


@app.route("/", method="GET")
def serve_form():
    info = {
        "title": "Welcome to the Teams Page",
        "teams": get_teams(db)
    }
    return template("teams_form.tpl", info, template_lookup=path_to_templates)


@app.route("/", method="POST")
def index(db):
    """Home Page"""
    info = {
        "title": "Welcome to the Teams Page",
        "teams": get_teams(db)
    }

    return template("team_creation_confirmation.tpl", info, template_lookup=path_to_templates)


@app.route("/team_creation", method="POST")
def team(db):
    """Process like form request"""
    teams = request.forms.get("teams")

    # If there is a value in the like field
    if teams:
        # store it in the db
        store_team_name(db, teams)

    # query the db for a return page
    info = {
        "title": "Welcome to the Teams Page",
        "teams": get_teams(db)
    }
    # display a return page
    return template("team_creation_confirmation.tpl", info, template_lookup=path_to_templates)


if __name__ == "__main__":
    DATABASE_NAME = "test.db"
    db = sqlite3.connect(DATABASE_NAME)

    """The database plugin is used to manage the connection and route handlers"""
    plugin = bottle_sqlite.Plugin(dbfile=DATABASE_NAME)
    app.install(plugin)

    app.run(debug=True)
