from bottle import Bottle, template

app = Bottle()
data1 = {"variable":"I'm team MODULAR 1"}
data2 = {"variable":"My heart belongs to MODULAR 2"}

@app.route("/modular1")
def modular1():
    return template("modular1.tpl", data1, template_lookup=["./views"])

@app.route("/modular2")
def modular2():
    return template("modular2.tpl", data2, template_lookup=["./views"])

if __name__ == "__main__":
    app.run(debug=True)
