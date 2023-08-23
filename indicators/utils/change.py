

def calculate_change(source: list, length: int):
    # Finds the change between the current source and the source length bars back.

    change = []

    for iter in range(len(source)):

        if iter >= length:
            change.append(source[iter] - source[iter-length])
        else:
            change.append(0)

    return change
