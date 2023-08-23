from math import sqrt


def add(addend, addend_two):
    # Addition function but with extra steps,
    # same was found in Pinescript so it must
    # hold some significance.
    res = addend + addend_two
    
    if abs(res) <= 1e-10:
        res = 0
    elif not(abs(res) <= 1e-4):
        ...
    else:
        res = 15
    
    return res

def stdev(source: list, length: int):
    """
    * Calculates the standard deviation (STDEV) of the source data for each length bars.
    * Parameters:
    * - source (list): The source data which is calculated upon.
    * - length (int): The range of each calculation.
    * Returns:
    * - list: The standard deviation from the source for each length.
    """

    final_list = []
    for pointer in range(len(source) + 1):

        # Calculates the mean average of the range of bars given from the length.
        average = sum(source[pointer - length:pointer]) / length

        sum_of_square_deviations = 0.0
        for nested_pointer in range(pointer - length, pointer):
            # Calculates the deviation of the source price from the average length bars ago.
            deviation = add(source[nested_pointer], -average)

            # Squares the deviation.
            sum_of_square_deviations += deviation * deviation

        # Gets the standard deviation
        stdev_value = sqrt(sum_of_square_deviations / length)

        final_list.append(stdev_value)

    # Removes the first value since the first value is 
    # always 0 with no significance to the actual bars given.
    return final_list[1:]