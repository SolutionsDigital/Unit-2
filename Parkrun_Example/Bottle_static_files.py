from bottle import Bottle, static_file

app = Bottle()

"""This enables an httprequest to http://127.0.0.1:8080/static/images/parkrun.png"""
@app.route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == '__main__':
    app.run(debug=True)
