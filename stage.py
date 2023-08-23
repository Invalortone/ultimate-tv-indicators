from tvDatafeed import TvDatafeed, Interval
import indicators

username = "Invalortone"
password = "Propper314"

tv = TvDatafeed(username, password)

data_frame    = tv.get_hist(symbol="BINANCE:BTCUSDT", interval=Interval.in_1_minute, n_bars=100000)
data_frame_3H = tv.get_hist(symbol="BINANCE:BTCUSDT", interval=Interval.in_3_hour, n_bars=100000)

close_prices = list(data_frame['close'])
close_prices_3H = list(data_frame_3H['close'])
open_prices  = list(data_frame['open'])
high_prices  = list(data_frame['high'])
low_prices   = list(data_frame['low'])


print(indicators.Xpi_cycle(close_prices, close_prices_3H))
