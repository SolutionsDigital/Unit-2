from bottle import Bottle, template

app= Bottle()

@app.route("/conditionals")
def condition_if():
    """The template function takes a dictionary as a parameter so even checking a boolean has to be
    done through a dictionary. The key is the name of the variable in the .tpl file the value is the
    boolean value"""
    admin_check = {'is_staff':'yes'}
    return template("conditional_if.tpl", admin_check, template_lookup=["./views"])

if __name__ == '__main__':
    app.run(debug=True)
