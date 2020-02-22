from bottle import Bottle, template, request
path_yo_templates = ["./views"]
app=Bottle()

@app.route("/")
def index():
    """Home page"""
    info = {
        "result":None
    }
    return template("form_convert.tpl", info, template_lookup=path_to_templates)

@app.route("/convert")
def convert_currency():
    """Process form data and return template page with result of conversion"""
    amount = request.query.get("amount", type=float)
    currency = request.query.get("currency")
    info = {
        "amount":amount,
        "currency":currency,
        "result": convert(amount,currency)
    }
    return template("form_convert.tpl",info, template_lookup=path_yo_templates)

def convert(amount,currency):
    """convert an amount of some currency into AUD
    return the amount as float"""
    exchange_rates={
        "USD":1.41,
        "GBP":1.88,
        "EUR":1.60
    }
    if currency in exchange_rates:
        return amount*exchange_rates[currency]
    else:
        return 0.0

if __name__=="__main__":
    app.run(debug=True)
