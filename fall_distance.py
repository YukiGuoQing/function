def fall_distance(val):
    """
    This function calculates d = (1/2)g*val*val g=9.8
    """
    return val * val * 0.5 * 9.8


dist = fall_distance(3.2)


print(dist)
