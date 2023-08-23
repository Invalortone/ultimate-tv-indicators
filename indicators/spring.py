

def spring(source_high: list, source_low: list, scanning_length: int = 200) -> tuple:
    """
    * Spring function based on the indicator Spring with Tanning Lines by Iceberg.
    * Parameters:
    * - source_high (list): The source data representing the highes.
    * - source_low (list): The source data representing the lows.
    * - scanning_length (int): The length which is sued to scan the sources.
    * Returns:
    * 1. list: The Spring.
    * 2. list: The UTAD.
    """

    # Defines the main two arrays of data which will be the objective of this indicator.
    spring = []
    utad   = []

    for high_value, low_value in zip(range(len(source_high)), range(len(source_low))):
        # Iterates through the high and low prices.

        if high_value > scanning_length:
            # Gets the highest value from the highes, 200 values back.
            utad.append(max(source_high[high_value - scanning_length:high_value]))

        if low_value > scanning_length:
            # Gets the lowest value from the lows, 200 values back.
            spring.append(min(source_low[low_value - scanning_length:low_value]))

    return (spring, utad)