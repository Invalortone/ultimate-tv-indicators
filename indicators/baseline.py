

def donchian(source_low, source_high, length):

    # First, it finds the lowest of
    # `length` bars back.
    minimums = []
    for min_index in range(len(source_low)):
        # This `if statement` is to neglect the
        # items that dont have enough values before it.
        if min_index >= length:
            lowest = min(source_low[(min_index + 1) - length:min_index + 1])
            minimums.append(lowest)
        else:
            minimums.append(0.0)

    # In contrast, this finds the
    # highest of `length` bars back.
    maximums = []
    for max_index in range(len(source_high)):
        if max_index >= length:
            highest = max(source_high[(max_index + 1) - length:max_index + 1])
            maximums.append(highest)
        else:
            maximums.append(0.0)

    # Finds the average of the lowest and the highest
    result = [(minimum + maximum) / 2 for minimum, maximum in zip(minimums, maximums)]

    return result


def baseline(source_low: list, source_high: list, base_periods: int = 26) -> list:
    """
    * Baseline function calculates based on the Ichimoku Cloud version of a baseline.
    * Parameters:
    * - source_low (list): The source data representing the lows.
    * - source_high (list): The source data representing the highes.
    * - base_periods (int): The length of the donchian channel.
    * Returns:
    * - list: The Base Line data list.
    """

    # The Baseline is just a donchian.
    base_line = donchian(source_low, source_high, base_periods)

    return base_line

