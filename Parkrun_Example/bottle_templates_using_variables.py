from bottle import Bottle, template

app = Bottle()

"""Using python expressions in placeholders"""

"""Content of variable 'name' is lowercased """
tpl1 = "Hello {{name.lower()}}"
"""Content of variable 'Title' is titlecased"""
tpl2 = "{{title.title()}}"
"""Id the value of the variable 'name' is null then "Default" is displayed"""
tpl3 = "{{name or 'Default'}}"
"""If the varibale is not diplayed and nothing is passed on to the template function other
than the template itself, "Nothing" is displayed.
defined is a function of the template engine to test if a variable exists"""
tpl4 = "{{name if defined('name') else 'Nothing'}}"

@app.route('/lower')
def lower():
    info = {'name': 'World'
            }
    return template(tpl1, info)

@app.route('/title')
def title():
    info = {'title':'the taming of the shrew'}

@app.route('/default')
def default():
    """The value for the key "name" is null"""
    info = {'name':''}
    return template(tpl3, info)

@app.route('/undefined')
def undefined():
    # info = {'name': 'Hello world'}
    # return template(tpl4, info)

    return template(tpl4)

if __name__ == '__main__':
    app.run(debug=True)
