from bottle import Bottle, request

app = Bottle()

def dict_to_html(a_dictionary):
    """the function takes a dictionary as a parameter and returns all key/value pairs
    in that dictionary formatted in as an unordered list in html"""


    html = "<ul>"
# """need to freeze the dictionary into a list (via the list() function to avoid an error here"""
    for key in list(a_dictionary):
        """using %s for string formatting. %s are placeholders and the values are passed after the string """
        html += "<li><strong>%s: </strong>%s</li>" % (key, a_dictionary[key])
    html += "</u>"
    return html

@app.route('/about')
def about():
    result = dict_to_html(request.environ)

    return result

if __name__ == '__main__':
    app.run(debug=True)
