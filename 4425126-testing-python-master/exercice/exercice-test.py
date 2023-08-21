def to_absolute(number):
    """ 
    >>> to_absolute(3)
    3

    >>> to_absolute(-5)
    5
    """
    if number <= 0:
        return -number
    return number


