def sum(source, length):
    # Gets the total sums of a range of items.
    full_sums = []
    for pointer in range(len(source)):
        # Iterates through the source as an index.
        total = 0

        for lookback in range(length):
            # Iterates through all items length bars back the current item
            total += source[pointer-lookback]

        full_sums.append(total)

    return full_sums

def calculateChange(source: list, length: int):
    # Finds the change between the current source and the source length bars back.

    change = []

    for iter in range(len(source)):
        
        if iter >= length:
            change.append(source[iter] - source[iter-length])
        else:
            change.append(0)

    return change

def kama(source: list, length: int = 13, fast_length: int = 10, slow_length: int = 26):
    """
    * Kaufman's Adaptive Moving Average, originally developed by Perry J. Kaufman, is used to identify the overall trend.
    * Parameters:
    * - source (list): The source data which will be calculated upon.
    * - length (int): The length used to calculate the change.
    * - fast_length (int): The length used to calculate the fast Alpha.
    * - slow_length (int): The length used to calculate the slow Alpha.
    * Returns:
    * - list: The KAMA (Kaufman's Adaptive Moving Average) list of data.
    """

    
    momenta_list = [abs(change) for change in calculateChange(source, length)]

    volatilities_list = sum([abs(change) for change in calculateChange(source, 1)], length)

    efficiency_ratioes = [momentum / (volatility if volatility != 0 else 1) for momentum, volatility in zip(momenta_list, volatilities_list)]

    fast_alpha = 2 / (fast_length + 1)
    slow_alpha = 2 / (slow_length + 1)

    alphas = [(efficiency_ratio * (fast_alpha - slow_alpha) + slow_alpha) ** 2 for efficiency_ratio in efficiency_ratioes]


    kaufman_ma = [source[0]]

    for alpha, source_value, pointer in zip(alphas, source, range(len(source))):
        kaufman_ma.append(alpha * source_value + (1 - alpha) * kaufman_ma[pointer])

    return kaufman_ma