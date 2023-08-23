from .utils.moving_averages import ema


def alpha(length):
    return 2 / (length + 1)

def equalize(source, fast_length, slow_length):
    # Purely mathematical procedures
    alpha_fast = alpha(fast_length)
    alpha_slow = alpha(slow_length)

    the_x = []
    for fast_ema, slow_ema in zip(ema(source, fast_length)[1:-1], ema(source, slow_length)[1:-1]):
        the_x.append((alpha_fast * fast_ema - alpha_slow * slow_ema) / (alpha_fast - alpha_slow))
    
    return the_x

def level(level, source, fast_length, slow_length):
    # Purely mathematical procedures
    alpha_fast = alpha(fast_length)
    alpha_slow = alpha(slow_length)

    the_x = []
    for fast_EMA, slow_EMA in zip(ema(source, fast_length)[1:-1], ema(source, slow_length)[1:-1]):
        the_x.append((level + (1 - alpha_slow) * slow_EMA - (1 - alpha_fast) * fast_EMA) / (alpha_fast - alpha_slow))
    
    return the_x

def cross_ema(P, V, X, Y, Z):
    # Purely mathematical procedures

    PX_emaList = ema(P, X)
    PY_emaList = ema(P, Y)
    VZ_emaList = ema(V, Z)
    the_X = []
    xyz = 0
    for PX_ema, PY_ema, VZ_ema in zip(PX_emaList, PY_emaList, VZ_emaList):
        new_X = (PX_emaList[xyz-1] * alpha(X) * alpha(Z) - PY_emaList[xyz-1] * alpha(Y) * alpha(Z) - PX_emaList[xyz-1] * alpha(X) + PY_emaList[xyz-1] * alpha(Y) + PY_emaList[xyz-1] * alpha(Z) + VZ_emaList[xyz-1] * alpha(Z) - PX_emaList[xyz-1] * alpha(Z) - PY_emaList[xyz-1] - VZ_emaList[xyz-1] + PX_emaList[xyz-1]) / (alpha(X) * alpha(Z) - alpha(Y) * alpha(Z) - alpha(X) + alpha(Y))
        the_X.append(new_X)
        xyz += 1
    return the_X

def rmacd(source: list, fast_length: int = 12, slow_length: int = 26, ema_length: int = 9, midline_length: int = 0):
    """
    * The RMACD function is based on the indicator by the name CT Reverse MACD Cross by The_Caretaker.
    * Parameters:
    * - source (list): The source data which will be calculated upon.
    * - fast_length (int): The length used to calculate the fast alpha.
    * - slow_length (int): The length used to calculate the slow alpha.
    * - ema_length (int): The length for the slow MA
    * - midline_length (int): The length for the zero line level.
    * Returns:
    * 1. list: The Signal MACD line.
    * 2. list: The Zero Line MACD line.
    * 3. list: The Reverse MACD line.
    """

    fast_moving_averages = ema(source, fast_length)
    slow_moving_averages = ema(source, slow_length)

    macd = [fast_ema - slow_ema for fast_ema, slow_ema in zip(fast_moving_averages, slow_moving_averages)]

    signal_macd    = cross_ema(source, macd, fast_length, slow_length, ema_length)
    zero_line_macd = level(midline_length, source, fast_length, slow_length)
    reverse_macd   = equalize(source, fast_length, slow_length)

    return (signal_macd, zero_line_macd, reverse_macd)