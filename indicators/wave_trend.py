from .utils.moving_averages import ema, sma

def wavetrend(source_high: list, source_low: list, source_close: list, channel_length: int = 10, average_length: int = 21) -> tuple:
    """
    * Calculates the WaveTrend by LazyBear indicator which is a port of a famous TS/MT indicator.
    *
    Parameters:
    * - source_high (list): The source data of the High.
    * - source_low (list): The source data of the Low.
    * - source_close (list): The source data of the Close.
    * - channel_length (int): The period for the moving average channel.
    * - average_length (int): The period for the green wave trend.
    Returns:
    * 1 list: The Green wave oscillator
    * 2 list: The Red wave oscillator
    """

    # The mean average between the Highes, Lows and the Close 
    hlc3_source = [(high_value + low_value + close_value) / 3 for high_value, low_value, close_value in zip(source_high, source_low, source_close)]
 
    # The exponential moving average for the source.
    exponential_source = ema(hlc3_source, channel_length)

    # Gets the absolute difference between the source and the exponential source and finds its exponential moving average.
    absolute_diff_list = [abs(source_value - exponential_value) for source_value, exponential_value in zip(hlc3_source, exponential_source)]
    exponential_diff_list = ema(absolute_diff_list, channel_length)

    # Lowers the values by 1.5% of its original value.
    exponential_divisors = [0.015 * exponential_diff for exponential_diff in exponential_diff_list]
    # Gets the difference between the source and the exponential.
    difference_dividends = [source_value - exponential_value for source_value, exponential_value in zip(hlc3_source, exponential_source)]

    # Dividedes the difference and the exponential value (if its not 0 to avoid division by zero errors) 
    # ! Warning: Im not sure if 'compound_interest' is the correct variable name since its name on the Pinescript indicator was CI so I inferred it.
    compounded_interest = [diff_value / (expo_value if expo_value else 1) for diff_value, expo_value in zip(difference_dividends, exponential_divisors)]

    # Defines the green oscillator and the red oscillator
    green_wave = ema(compounded_interest, average_length)
    red_wave   = sma(green_wave, 4, True)

    return (green_wave, red_wave)

def double_wavetrend(source_high: list, source_low: list, source_close: list, channel_length_fast: int = 15, average_length_fast: int = 11, channel_length_slow: int = 50, average_length_slow: int = 21) -> tuple:
    """
    * Calculates the double wavetrend oscillator modified by Mynicknameislion on TradingView.
    *
    Parameters:
    * - source_high (list): The source for the high data.
    * - source_low (list): The source for the low data.
    * - source_close (list): The source for the close data.
    * - channel_length_fast (int): The channel length for the fast wave trend.
    * - average_length_fast (int): The average length for the fast wave trend.
    * - channel_length_slow (int): The channel length for the slow wave trend.
    * - average_length_slow (int): The average length for the slow wave trend.
    Returns:
    * - list: Fast Wave Trend data.
    * - list: Slow Wave Trend data.
    """
    
    fast_wave = wavetrend(source_high, source_low, source_close, channel_length_fast, average_length_fast)[0]
    slow_wave = wavetrend(source_high, source_low, source_close, channel_length_slow, average_length_slow)[0]

    return (fast_wave, slow_wave)

