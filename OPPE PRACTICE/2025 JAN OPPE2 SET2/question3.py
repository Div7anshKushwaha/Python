def same_sign(a, b):
    """
    Checks whether two numbers have the same sign.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if the numbers have the same sign, False otherwise.

    Examples:
        >>> same_sign(10, 20)
        True
        >>> same_sign(-5, -15)
        True
        >>> same_sign(0, 0)
        True
        >>> same_sign(10, -20)
        False
        >>> same_sign(0, 10)
        False
    """
    if a== 0 and b == 0:
        return True
    if a== 0 or b==0:
        return False
    return (a>0 and b>0) or (a<0 and b<0)    
    