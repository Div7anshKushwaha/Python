def number_with_more_unique_digits(n1:int, n2:int):
    """
    Compares two integers and returns the one with more unique digits.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int or tuple: The integer with more unique digits. 
        If both numbers have the same number of unique digits, 
        returns a tuple of both integers `(n1, n2)`.

    Example:
        >>> number_with_more_unique_digits(123, 1122)
        123

        >>> number_with_more_unique_digits(1122, 2211)
        (1122, 2211)
    """
    s1 = str(n1)
    s2 = str(n2)
    l1 = len(set(s1))
    l2 = len(set(s2))
    if l1>l2:
        return n1
    elif l2>l1:
        return n2
    else:
        return (n1,n2)