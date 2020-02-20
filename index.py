from flask import Flask, jsonify, request

app = Flask(__name__)

prices = [
    {'description': 'website', 'amount': 0}
]


@app.route('/prices')
def get_prices():
    return jsonify(prices)


@app.route('/prices', methods=['POST'])
def add_price():
    prices.append(request.get_json())
    return '', 204
