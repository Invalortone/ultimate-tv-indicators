from .rsi import rsi
from .stdev import stdev
from .moving_averages import sma

def calculate_tdigm(source: list, rsi_period: int = 21, band_length: int = 34, length_rsi_fast: int = 7, length_rsi_slow: int = 2):
    """
    * Calculates the Traders Dynamic Index made by Goldminds on Tradingview.
    *
    Parameters:
    * - source (list): The source data calulated upon.
    * - rsi_period (int): The length for the RSI.
    * - band_length (int): The upper/lower/middle band length.
    """

    rsi_list = rsi(source, rsi_period)
    
    ma_list = sma(rsi_list, band_length, True)
    fib_deviation = [price * 1.6185 for price in stdev(rsi_list, band_length)]
    
    upper_band = [sma_price + fib_price for fib_price, sma_price in zip(fib_deviation, ma_list)]
    lower_band = [sma_price - fib_price for fib_price, sma_price in zip(fib_deviation, ma_list)]

    

    middle_band = [(upper_value + lower_value) / 2 for upper_value, lower_value in zip(upper_band, lower_band)]

    fastMA = sma(rsi_list, length_rsi_fast, True)
    slowMA = sma(rsi_list, length_rsi_slow, True)

    return (fastMA, slowMA, upper_band, lower_band, middle_band)
    