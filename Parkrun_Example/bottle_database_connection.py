import sqlite3
from bottle import Bottle, template, request
app=Bottle()
path_to_templates= ["./views"]

@app.route("/")
def index():
    return "Welcome to Parkrun Teams."

@app.route("/teams")
def todo_list():
    conn = sqlite3.connect("parkrun_db.db")
    c = conn.cursor()
    c.execute("SELECT TeamName, TeamCaptainID FROM Teams")
    result = c.fetchall()
    c.close()
    return template("new_team.tpl", rows=result, template_lookup=path_to_templates)

@app.route("/teams", method="Post")
def newteam_handler():
    """Handle the form submission"""
    # get the input from the form
    newteamname = request.forms.get("newteam")
    # add it to a list as it needs to be passed as a list to the sql statement apparently! To check
    newteam = []
    newteam.append(newteamname)
    print(newteam)

    conn = sqlite3.connect("parkrun_db.db")
    c = conn.cursor()
    # This SQL INSERT Statement does not work
    c.execute("INSERT INTO Teams (TeamName) VALUE (?)", [newteam])
    result = c.fetchall()
    c.close()
    return template("new_team.tpl", rows=result, template_lookup=path_to_templates)

if __name__=="__main__":
    app.run(debug=True)

