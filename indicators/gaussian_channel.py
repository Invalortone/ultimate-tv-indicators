from .utils.true_ranges import tr
from math import cos, sqrt, pow, asin

def filter_data(modifier, source, selector):
    # Filters the raw data given into clean data to be used to calculate the poles.
    
    # Sets the difference between the modifier and 1
    difference = (1 - modifier)

    # Defines the various multipliers depending on the selector's value
    multiplier_2 = 36  if selector == 9 else 28 if selector == 8 else 21 if selector == 7 else 15 if selector == 6 else 10 if selector == 5 else 6 if selector == 4 else 3 if selector == 3 else 1 if selector == 2 else 0
    multiplier_3 = 84  if selector == 9 else 56 if selector == 8 else 35 if selector == 7 else 20 if selector == 6 else 10 if selector == 5 else 4 if selector == 4 else 1 if selector == 3 else 0
    multiplier_4 = 126 if selector == 9 else 70 if selector == 8 else 35 if selector == 7 else 15 if selector == 6 else 5  if selector == 5 else 1 if selector == 4 else 0
    multiplier_5 = 126 if selector == 9 else 56 if selector == 8 else 21 if selector == 7 else 6  if selector == 6 else 1  if selector == 5 else 0 
    multiplier_6 = 84  if selector == 9 else 28 if selector == 8 else 7  if selector == 7 else 1  if selector == 6 else 0 
    multiplier_7 = 36  if selector == 9 else 8  if selector == 8 else 1  if selector == 7 else 0 
    multiplier_8 = 9   if selector == 9 else 1  if selector == 8 else 0 
    multiplier_9 = 1   if selector == 9 else 0

    # Creates the base values which upon them will be filtered and modified
    base_values = [pow(modifier, selector) * s for s in source]
    
    filtered_data = [base_values[0]]
    
    for base_lookback in range(len(base_values) - 1):
        # Calculates the basic filtration level with the multiplier of 1
        filtered_datum = (filtered_data[base_lookback] * difference * selector ) + base_values[base_lookback+1]

        # Defines all cases needed to change the filtered data 
        # based on the selector and the multipliers.
        if selector >= 2 and base_lookback >= 1:
            filtered_datum -= (multiplier_2 * pow(difference, 2) * filtered_data[base_lookback - 1])

        if selector >= 3 and base_lookback >= 2:
            filtered_datum += (multiplier_3 * pow(difference, 3) * filtered_data[base_lookback - 2])

        if selector >= 4 and base_lookback >= 3:
            filtered_datum -= (multiplier_4 * pow(difference, 4) * filtered_data[base_lookback - 3])

        if selector >= 5 and base_lookback >= 4:
            filtered_datum += (multiplier_5 * pow(difference, 5) * filtered_data[base_lookback - 4])

        if selector >= 6 and base_lookback >= 5:
            filtered_datum -= (multiplier_6 * pow(difference, 6) * filtered_data[base_lookback - 5])

        if selector >= 7 and base_lookback >= 6:
            filtered_datum += (multiplier_7 * pow(difference, 7) * filtered_data[base_lookback - 6])

        if selector >= 8 and base_lookback >= 7:
            filtered_datum -= (multiplier_8 * pow(difference, 8) * filtered_data[base_lookback - 7])

        if selector == 9 and base_lookback >= 8:
            filtered_datum += (multiplier_9 * pow(difference, 9) * filtered_data[base_lookback - 8])

        filtered_data.append(filtered_datum)
    
    

    return filtered_data



def find_poles(modifier, source, selector):
    # Calculates the poles for the Guasciann Channel after filtering the data provided.
   
    
    # Calulates all of the filtered data based on the selector.
    # filtered_data_1 is the south pole.
    filtered_data_1, filtered_data_2, filtered_data_3 = (filter_data(modifier, source, 1)),                       (filter_data(modifier, source, 2) if selector >= 2 else 0), (filter_data(modifier, source, 3) if selector >= 3 else 0)
    filtered_data_4, filtered_data_5, filtered_data_6 = (filter_data(modifier, source, 4) if selector >= 4 else 0), (filter_data(modifier, source, 5) if selector >= 5 else 0), (filter_data(modifier, source, 6) if selector >= 6 else 0)
    filtered_data_7, filtered_data_8, filtered_data_9 = (filter_data(modifier, source, 7) if selector >= 7 else 0), (filter_data(modifier, source, 8) if selector >= 8 else 0), (filter_data(modifier, source, 9) if selector == 9 else 0)

    # Defines the north pole based on the selector
    if selector == 1:
        north_pole = filtered_data_1

    elif selector == 2:
        north_pole = filtered_data_2

    elif selector == 3:
        north_pole = filtered_data_3

    elif selector == 4:
        north_pole = filtered_data_4

    elif selector == 5:
        north_pole = filtered_data_5

    elif selector == 6:
        north_pole = filtered_data_6

    elif selector == 7:
        north_pole = filtered_data_7

    elif selector == 8:
        north_pole = filtered_data_8

    elif selector == 9:
        north_pole = filtered_data_9

    else:
        # Else, the nnorth pole won't equal to anything.
        north_pole = 0
    

    return (north_pole, filtered_data_1)

def gaussian_channel(source_close: list, source_high: list, source_low: list, percentage: int = 144, selector: int = 4, multiplier: float = 1.414) -> tuple:
    """
    * The Gaussian Channel function is based on an indicator with the same name by DonovanWall
    * Parameters:
    * - source_close (list): The sourse code representing the closes.
    * - source_high (list): The sourse code representing the highes.
    * - source_low (list): The sourse code representing the lows.
    * - percentage (int): Constant which calculated the beta.
    * - selector (int): Also known as the number of poles.
    * - multiplier (float): The multiplier.
    * Returns:
    * 1. list: The High Band.
    * 2. list: The Middle Band.
    * 3. list: The Low Band.
    """

    complete_source = []

    for close_value, high_value, low_value in zip(source_close, source_high, source_low):
        # Calculates the mean average between the close, high, and low which creates the HLC3
        complete_source.append((close_value + high_value + low_value) / 3)

    # Defines the alpha and beta which are two core 
    # mathematical constants that serve great purpose in this indicator.
    beta  = (1 - cos(4 * asin(1) / percentage)) / (pow(1.414, 2 / selector) - 1)
    alpha = (-1 * beta) + sqrt(pow(beta, 2) + 2 * beta)

    # Finds the true range between the HLC3
    trdata = tr(source_high, source_low, source_close)

    # Defines the poles of HLC3 and the true range.
    (filter, _)            = find_poles(alpha, complete_source, selector)
    (filter_true_range, _) = find_poles(alpha, trdata, selector)

    high_band = []
    low_band  = []

    # Calculates the high_band and the low_band where the price ricochets from
    for filt_value, filttr_value in zip(filter, filter_true_range):
       
        high_band.append(filt_value + filttr_value * multiplier)
        low_band .append(filt_value - filttr_value * multiplier)

    return (high_band, filter, low_band)