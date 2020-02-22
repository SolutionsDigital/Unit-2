from bottle import Bottle, template, request

path_to_templates = ["./views"]
app = Bottle()
@app.route("/using_forms")
def serve_form():
    """
    serve the form with a prompt message first
    This function is run when a GET request is received
    GET is the default method that bottle handles requests (see console messages)
    """
    return template("form.tpl", message="Please enter your name", template_lookup=path_to_templates )

@app.route("/using_forms", method="POST")
def handle_form():
    """ Handle the form submission"""
    first = request.forms.get("first")
    last = request.forms.get("last")
    hello_message = "Hello " + first + " " + last +"."

    return template("form.tpl", message=hello_message,template_lookup=path_to_templates)

if __name__=="__main__":
    app.run(debug=True)
