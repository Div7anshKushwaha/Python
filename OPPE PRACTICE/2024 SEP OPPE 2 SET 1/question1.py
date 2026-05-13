def is_even_two_digit_number(num):
    """
    Determines whether a given number is an even two-digit number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if `num` is an even two-digit number, False otherwise.

    Examples:
        >>> is_even_two_digit_number(42)
        True
        >>> is_even_two_digit_number(99)
        False
        >>> is_even_two_digit_number(-48)
        True
        >>> is_even_two_digit_number(5)
        False
    """
    if ((10<= abs(num) <100) and (num%2 == 0)):
        return True
    else:
        return False    