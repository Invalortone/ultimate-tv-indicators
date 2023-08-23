from .utils.change import calculate_change
from .utils.true_ranges import tr
from .utils.moving_averages import rma

def dmi_adx(source_high: list, source_low: list, source_close: list, length: int = 14, signal_length: int = 2) -> tuple:
    """
    * The DMI_ADX function is based on the Directional Movement Index indicator by Tradingview.
    * Parameters:
    * - source_high (list): The source data that represents the highes.
    * - source_low (list): The source data that represents the lows.
    * - source_close (list): The source data that represents the closes.
    * - length (int): The DI length.
    * - signal_length (int): The ADX Smoothing length.
    * Returns:
    * 1. list: The DI+ list.
    * 1. list: The DI- list.
    * 1. list: The ADX list.
    """

    # Calculates the change of the lows and the highes. The low change should be negative.
    low_changes = [-low_change for low_change in calculate_change(source_low, 1)]
    high_changes = calculate_change(source_high, 1)
    
    plus_direction = []

    for high_change, low_change in zip(high_changes, low_changes):
        # Checks if the high change is positive and above the low change
        if (high_change > low_change and high_change > 0):
            plus_direction.append(high_change)

        else:
            plus_direction.append(0)

    minus_direction = []

    for high_change, low_change in zip(high_changes, low_changes):
        # Checks if the low cahnge is positive and above the high change.
        if (low_change > high_change and low_change > 0):
            minus_direction.append(low_change)
        
        else:
            minus_direction.append(0)

    # Calculates the rolling moving average of the true range, also known as the TRUR.
    true_range_averages = rma(tr(source_high, source_low, source_close), length)

    directional_positive = []

    for plus_value, true_range_average in zip(rma(plus_direction, length), true_range_averages):
        # Calculates the percentage for the plus value. 
        plus_percent = 100 * plus_value / true_range_average

        directional_positive.append(plus_percent)

    directional_negative = []

    for minus_value, true_range_average in zip(rma(minus_direction, length), true_range_averages):
        # Calculates the percentage for the minus value.
        minus_percent = 100 * minus_value / true_range_average

        directional_negative.append(minus_percent)


    directional_neutral = []

    for positive, negative in zip(directional_negative, directional_positive):
        # The neutral direction is by adding the negative with the positive
        directional_neutral.append(negative + positive)

    adx_source = []
    for negative, positive, neutral in zip(directional_negative, directional_positive, directional_neutral):
        
        if neutral == 0:
            adx_src_value = 1

        else:
            adx_src_value = neutral

        # Formula for the source of the ADX list
        adx_source.append(abs(positive - negative) / adx_src_value)

    adx = []
    # Calculates the rolling moving average of the ADX.
    for adx_avg in rma(adx_source, signal_length):
        adx.append(100 * adx_avg)

    return (directional_positive, directional_negative, adx)
