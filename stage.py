from tvDatafeed import TvDatafeed, Interval
import indicators

username = "Invalortone"
password = "Propper314"

tv = TvDatafeed(username, password)

data_frame = tv.get_hist(symbol="BINANCE:BTCUSDT", interval=Interval.in_daily, n_bars=100000)

close_prices = list(data_frame['close'])
open_prices  = list(data_frame['open'])
high_prices  = list(data_frame['high'])
low_prices   = list(data_frame['low'])


print(indicators.calculate_tdigm(close_prices))