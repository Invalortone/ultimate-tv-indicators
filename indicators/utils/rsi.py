from .moving_averages import rma

def rsi(source: list, length: int) -> list:
    """
    * Relative strength index. It is calculated based on rma's of upward and downward change of x.
    * Parameters
    * - source (list): The source data which is calculated upon.
    * - length (int): The range of each calculation.
    * Returns
    * - list: The Relative Strength Index (RSI) list.
    """

    upper_band = []
    lower_band = []
    for pointer in range(len(source)):
        # Gets the difference between two consecutive source values
        upward   = max(source[pointer] - source[pointer-1], 0)
        downward = max(source[pointer-1] - source[pointer], 0)

        upper_band.append(upward)
        lower_band.append(downward)

    # Defines the running moving average (RMA) of each band
    upper_rma = rma(upper_band, length)
    lower_rma = rma(lower_band, length)

    final_list = []
    for upper_value, lower_value in zip(upper_rma, lower_rma):
        # Checks if its not None or 0
        if upper_value and lower_value:
            
            # Calculates the Relative Strength Index by the formula,
            # RSI = (100 - 100 / (1 + upper_band / lower_band))
            middle_fraction = upper_value / lower_value
            rsi_value = 100 - 100 / (1 + middle_fraction)

            final_list.append(rsi_value)

        else:
            final_list.append(0)

    return final_list