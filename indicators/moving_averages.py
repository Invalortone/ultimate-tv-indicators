import pandas as pd


def sma(source: list, length: int, has_null: bool = True) -> list:
    """
    * Calculate the Simple Moving Average (SMA) of a list of data.
    *  Parameters:
    * - source (list): The source data for the calculation.
    * - length (int): The range of each calculation
    * - has_null (bool): Decide if null entries should be included or not.
    * Returns:
    * - list: The SMA of the source data.
    """

    # Convert array of integers to pandas series
    numbers_series = pd.Series(source)

    # Get the window of series
    # of observations of specified window size
    windows = numbers_series.rolling(length)

    # Create a series of moving
    # averages of each window
    moving_averages = windows.mean()

    # Convert pandas series back to list
    moving_averages_list = moving_averages.tolist()

    # Remove null entries from the list
    final_list = moving_averages_list[length - 1:]

    # If the developer wants null entries it will be returned.
    return (moving_averages_list if has_null else final_list)


def ema(source: list, length: int) -> list:
    """
    * The ema function returns the exponentially weighted moving average. 
    * Parameters:
    * - source (list): The source data for the calculation.
    * - length (int): The range of each calculation.
    * Returns
    * - list: Exponential Moving Average list
    """

    # EMA Alpha
    alpha = 2 / (length + 1)

    # Sets the initial value of the ema list.
    final_list = [source[0]]
    
    for source_value, pointer in zip(source, range(len(source))):
        # Based on the formula, EMA = alpha * source + (1 - alpha) * EMA[1]
        final_list.append(alpha * source_value + (1 - alpha) * final_list[pointer])

    return final_list[1:]


def rma(source: list, length: int) -> list:
    """
    * It is the exponentially weighted moving average with alpha = 1 / length.
    * Parameters:
    * - source (list): The source data for calculations.
    * - length (int): The range of each calculation.
    * Returns:
    * - list: Running moving average (RMA) list.
    """
    # RMA Alpha
    alpha = 1.0 / length

    # Sets the initial value of the ema list.
    final_list = [source[0]]
    
    for source_value, pointer in zip(source, range(len(source))):
        # Based on the formula, RMA = alpha * source + (1 - alpha) * RMA[1]
        final_list.append(alpha * source_value + (1 - alpha) * final_list[pointer])

    return final_list