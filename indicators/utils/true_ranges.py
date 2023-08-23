from .moving_averages import rma

def tr(source_high: list, source_low: list, source_close: list) -> list:
    """
    * Calulates the true range between the highes and the lows between the closes.
    * Parameters:
    * - source_high (list): The source data of the highes.
    * - source_low (list): The source data of the lows.
    * - source_close (list): The source data of the closes.
    * Returns:
    * - list: The range of the highes, lows and the closes. 
    """

    final_list = []
    for high, low, previous_close in zip(source_high, source_low, range(len(source_close))):

        # Finds the max value between the range of high and low,
        # the range of high and close and the range of low and close.
        # This is known as the true range.
        tr_value = max(
            high - low,
            abs(high - source_close[previous_close-1]),
            abs(low - source_close[previous_close-1])
        )

        final_list.append(tr_value)

    return final_list


def atr(source_high: list, source_low: list, source_close: list, length: int) -> list:
    """
    * Calculates the Average true range (ATR) based on the RMA of the true range.
    * Parameters:
    * - source_high (list): The source of the high data.
    * - source_low (list): The source of the low data.
    * - source_close (list): The source of the close data.
    * - length (int): The range of each calculation.
    * Returns:
    * - list: 
    """

    # Gets the true range
    true_range = tr(source_high, source_low, source_close)

    # Finds the running moving average of the true range 
    # which is equivelant to the Average True Range.
    return rma(true_range, length)
