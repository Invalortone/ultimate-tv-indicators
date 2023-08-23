from .stdev import stdev
from .moving_averages import sma

def sharpe(source_low: list, source_high: list, source_close: list, source_open: list, length: int = 252, dividend_yield: float = 0.000, risk_free_rate: float = 0.0004) -> tuple:
    """
    * The Sharpe Function is based on the Trailing Sharpe Ratio indicator by Rashad
    * Parameters:
    * - source_low (list): The source data which represents the lows.
    * - source_high (list): The source data which represents the highes.
    * - source_close (list): The source data which represents the closes.
    * - source_open (list): The source data which represents the opens.
    * - length (int): Defines the length for the lookback period as well the deviation period.
    * - dividend_yield (float): The Dividend yield for the periodic change.
    * - risk_free_rate (float): Defines the rate of risk.
    * Returns:
    * 1. list: The Sharpe List
    * 2. list: The Signal List
    """

    # The HLCO4 List which is the average of all 4 sources.
    complete_sources = []
    for low_value, high_value, open_value, close_value in zip(source_low, source_high, source_open, source_close):
        complete_sources.append((low_value + high_value + open_value + close_value) / 4)

    # The change over a specified period of time.
    # ! I'm not sure if it's truly periodic change, I inferred it because the variable was called PC.
    periodic_change = []

    for source_value, lookback in zip(complete_sources[length:], range(len(complete_sources))):
        change = ((source_value - complete_sources[lookback]) / source_value) + dividend_yield*(length/252)

        periodic_change.append(change)

    # Gets the deviation from the sources over length bars
    deviations = stdev(complete_sources, length)

    # Turns it into a percentage
    percentages_of_deviation = [deviation / source_value for deviation, source_value in zip(deviations, complete_sources)]

    # Removes any extra list items to ensure both items are of equal length.
    percentages_of_deviation = percentages_of_deviation[len(percentages_of_deviation) - len(periodic_change):]

    # Calculates the Trailing Sharpe
    sharpe = []
    for change, percentage_deviation in zip(periodic_change, percentages_of_deviation):
        sharpe.append((change - risk_free_rate) / percentage_deviation)

    # Defines the signal as a simple moving average of the sharpe
    signal = sma(sharpe, length)

    return (sharpe, signal)
