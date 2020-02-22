from bottle import Bottle, response

app = Bottle()

@app.route("/html")
def responseToHtml():
    return "This is HTML. In the response, instructions are passed " \
           "to the browser to interpret this as <b>HTML</b>."

@app.route('/plain')
def responseToText():
    response.content_type = "text/plain"
    return "This is plain text. In the response, instructions are passed " \
           "to the browser to interpret this as plain text, not <b>HTML</b>."

if __name__ == "__main__":
    app.run(debug=True)


