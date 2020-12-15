from flask import Flask, render_template, request, flash
from forex import convert, get_currency_symbol, invalid_amount, invalid_from_code, invalid_to_code
app = Flask(__name__)
app.config["SECRET_KEY"] = "suppappappaseecrat"


@app.route('/')
def converter_form():
    from_currency = 'USD'
    to_currency = 'JPY'
    return render_template('index.html', from_currency=from_currency, to_currency=to_currency)


@app.route('/', methods=["POST"])
def convert_currency():
    # raise 
    from_currency = request.form['from']
    to_currency = request.form['to']
    amount = request.form.get("amount")
    # raise
    if invalid_amount(amount):
            flash('Invalid amount', 'error')
            
    try:
        
        result = convert(from_currency, to_currency, amount)
        symbol = get_currency_symbol(to_currency)
        return render_template('index.html', from_currency=from_currency, to_currency=to_currency, symbol=symbol, result=result)
    except:
        if invalid_from_code(from_currency):
            flash(f'Invalid currency: {from_currency}', 'error')
        if invalid_to_code(to_currency):
            flash(f'Invalid currency: {to_currency}', 'error')
        return render_template('index.html', from_currency=from_currency, to_currency=to_currency)

        