from bottle import Bottle, request, response, template
path_to_templates = ["./views"]

app = Bottle()
@app.route("/")
def index():
    info = {
        "title":"Welcome Home!",
        "content":"This is your first visit."
    }
    visits = request.get_cookie("visited")

    if visits:
        info['content'] = "you have been here before."

    response.set_cookie("visited","yes")

    return template("cookie_example.tpl", info, template_lookup=path_to_templates)

if __name__=="__main__":
    app.run(debug=True)
