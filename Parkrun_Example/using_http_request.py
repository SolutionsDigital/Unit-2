from bottle import Bottle, request

app = Bottle()

@app.route('/about')
def about():
    result = "<p>Your IP address is: " + request.remote_addr + "</p>"
    result += "<p>Your Broser is:" + request.environ['HTTP_USER_AGENT'] + "</p>"

    return result

if __name__ == '__main__':
    app.run(debug=True)
