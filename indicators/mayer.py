from .moving_averages import sma

def mayer(source: list, has_null: bool = True) -> list:
    """
    * Mayer function is based on the Mayer Multiple indicator by jacknyc and seeks to check if its a good time to invest in a token or not.
    * Parameters:
    * - source (list): The source data which will be calculated upon.
    * - has_null (bool): Contains NaN values?
    * Returns:
    * - list: The Mayer Multiple Histogram list.
    """

    # Mayer SMA
    mayer_sma = sma(source, 200, has_null)

    # Removes Null Values
    if (not(has_null)):
        source = source[200:]

    # Change over 200 bars ago
    mayer = [source_value / moving_avg_value for source_value, moving_avg_value in zip(source, mayer_sma)]

    return mayer
