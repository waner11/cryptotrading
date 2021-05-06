import config, csv, talib
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

candles = client.get_klines(symbol='MATICUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# csvfile = open('2018-2021.csv', 'w', newline='')
# candlestick_writer = csv.writer(csvfile, delimiter=',')

# for c in candles:
#     candlestick_writer.writerow(c)

# print(len(candles))

#candlesticks = client.get_historical_klines("MATICUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2018", "1 May, 2021")

#print(candlesticks)

# for candlestick in candlesticks:
#     candlestick_writer.writerow(candlestick)

# csvfile.close()