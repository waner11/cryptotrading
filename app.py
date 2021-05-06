from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv, talib
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

client = Client(config.API_KEY, config.API_SECRET)

@app.route('/')
def index():
    title = 'CoinView'

    account_info = client.get_account()

    balances = account_info['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('Index.html', title=title, my_balances=balances, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)

    try:
        order = client.create_order(
                symbol=request.form['symbol'],
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, 'error')

    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candlesticks = client.get_historical_klines("MATICUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 May, 2021")

    processed_candlesticks = []
    for data in candlesticks:
        candlestick = {
            "time": data[0],
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)