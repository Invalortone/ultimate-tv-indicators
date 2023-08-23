from .utils.moving_averages import sma


def minute_to_3hours(source):

    # Gets the average of each 180 items in a list, this is to allow comparison between 1 minute TF and 3 hour TF
    
    averages = []
    # Loops through the list every 18 item
    for i in range(0, len(source), 18):

        sublist = source[i:i+18]
        # Gets its mean average
        average = sum(sublist)/len(sublist)

        averages.append(average)

    return averages

def Xpi_cycle(source_1M: list, source_3H: list) -> tuple:
    """
    * XPI Cycle function which is based on the X Pi Cycle Alert by Iceberg.
    * Parameters:
    * - source_1M (list): The source data for 1 Minute TimeFrame which will be calculated upon.
    * - source_3H (list): The source data for 3 Hour TimeFrame which will be calculated upon.
    * Returns:
    * 1. list: The Low Near Data
    * 2. list: The Low Far Data
    * 3. list: The High Near Data
    * 4. list: The High Far Data
    """

    # Defines the two base sma's which will be calculated upon.
    lower_near_ma  = sma(source_1M, 471)
    higher_near_ma = sma(source_1M, 350)

    lower_near_data  = []
    higher_near_data = []

    for lower_near_ma_value, higher_near_ma_value in zip(lower_near_ma, higher_near_ma):
        # Iterates through each value in both sma's
        # Calculates their new values
        calculated_low_near = (lower_near_ma_value * 745) / 1000
        calculated_high_near = (higher_near_ma_value * 2)

        lower_near_data .append(calculated_low_near)
        higher_near_data.append(calculated_high_near)

    # Since this is a 1 minute dataframe, so we can compare
    # it with the 3 hours we must get the average of every 180 item. 3 * 60 = 180
    lower_near_data  = minute_to_3hours(lower_near_data)
    higher_near_data = minute_to_3hours(higher_near_data)

   

    # Defines the two base sma's which will be calculated upon but for the 3 hours version.
    lower_far_ma  = sma(source_3H, 471)
    higher_far_ma = sma(source_3H, 350)

    lower_far_data  = []
    higher_far_data = []

    for lower_far_ma_value, higher_far_ma_value in zip(lower_far_ma, higher_far_ma):
        # Iterates through the 2 sma's
        # Calculates the new values of the X PI Cycle
        calculated_low_far = (lower_far_ma_value * 745) / 1000
        calculated_high_far = (higher_far_ma_value * 2)

        lower_far_data.append(calculated_low_far)
        higher_far_data.append(calculated_high_far)

    return (lower_near_data, lower_far_data, higher_near_data, higher_far_data)