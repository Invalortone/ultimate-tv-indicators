from .rsi import rsi
from .stdev import stdev
from .moving_averages import sma

def calculate_tdigm(source: list, rsi_period: int = 21, band_length: int = 34, length_rsi_fast: int = 7, length_rsi_slow: int = 2):
    """
    * Calculates the Traders Dynamic Index made by Goldminds on Tradingview.
    * Parameters:
    * - source (list): The source data calulated upon.
    * - rsi_period (int): The length for the RSI.
    * - band_length (int): The upper/lower/middle band length.
    * -  length_rsi_fast (int): The Fast RSI length
    * -  length_rsi_slow (int): The Slow RSI length
    * Returns:
    * 1 list: The Fast MA
    * 2 list: The Slow MA
    * 3 list: The Upper Band
    * 4 list: The Middle Band
    * 5 list: The Lower Band
    """

    # Creates the RSI & SMA base lists.
    rsi_list = rsi(source, rsi_period)
    ma_list  = sma(rsi_list, band_length, True)

    # The Fast MA and the Slow MA are just simple moving averages 
    # with different lengths of the RSI List.
    fastMA = sma(rsi_list, length_rsi_fast, True)
    slowMA = sma(rsi_list, length_rsi_slow, True)

    # Finds the fibonacchi standard deviation for the RSI list.
    fib_deviation = [price * 1.6185 for price in stdev(rsi_list, band_length)]
    
    # Upper Band is calculated by adding the fibonacchi deviation and the sma
    # On the other hand, the Lower Band is calculated by subtracting the deviation
    # from the sma.
    upper_band = [sma_price + fib_price for fib_price, sma_price in zip(fib_deviation, ma_list)]
    lower_band = [sma_price - fib_price for fib_price, sma_price in zip(fib_deviation, ma_list)]

    # The middle band is the average between the upper band and the lower band.
    middle_band = [(upper_value + lower_value) / 2 for upper_value, lower_value in zip(upper_band, lower_band)]

    # Returns all 5 Lists as a tuple.
    return (fastMA, slowMA, upper_band, middle_band, lower_band)
    