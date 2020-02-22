from bottle import Bottle, template
app = Bottle()

"""The placeholder is in double {{}}"""
tpl = "Hello {{name}}!"

"""The template function requires the name of the template 
and the value for each placeholder in the template"""

@app.route("/about")
def about():
    return template(tpl, name='World')

"""Template taking several values as a dict"""
@app.route('/address')
def address():
    """passing a dictionary to the template function to instantiate several placeholders"""
    info={'number': '123', 'street': 'Fake St.', 'city': 'Fakeville'}
    tpl = 'I live at {{number}} {{street}}, {{city}}'
    return template(tpl, info)

"""Template referenced as an external file in the filesystem"""
path_to_template = ["./views"]
@app.route('/external')
def external():
    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }
    """template_lookup overrides bottle.TEMPLATE_PATH which has Linux style paths"""
    return template('simple.tpl', info, template_lookup=path_to_template)

if __name__ == '__main__':
    app.run(debug=True)
