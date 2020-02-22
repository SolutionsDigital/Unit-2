from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    return "This is the home page"

@app.route('/about')
def about(): 
    return "Tell me about yourself"

@app.route('/users/<who>')
def homepage(who):
    """generate a specific page for a specific user"""
    return "<p>This is the homepage for " + who + ".</p>"

# @app.route('/users/<who:path>')
# def homepage(who):
#     """generate a specific page for a specific user including html character entities
#        e.g. /users/%3Cb%hello%3C/b%3E%20there """
#     return "<p>This is the homepage for " + who + ".</p>"


if __name__ == '__main__':
    app.run(debug=True)
