from bottle import Bottle, response

app = Bottle()

@app.route("/plain")
def about():
    response.content_type = "text/plain"
    return "<b>This is what plain/text looks like</b>"

@app.route("/html")
def about():
    # response.content_type = "text/html"
    return "<b>This is what html looks like</b>"


if __name__ == '__main__':
    app.run(debug=True)
