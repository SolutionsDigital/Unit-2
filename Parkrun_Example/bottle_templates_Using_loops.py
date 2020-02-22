from bottle import Bottle, template

app = Bottle()

@app.route("/loop")
def loop():
    data = {
        "header": "Class list",
        "students":["Paul", "Ringo", "John", "George"]
    }
    return template("loop.tpl", data, template_lookup=["./views"])

if __name__ == '__main__':
    app.run(debug=True)
