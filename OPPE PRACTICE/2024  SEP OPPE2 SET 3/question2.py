def is_divisible_by_last_two_digits(num: int):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
    
        bool: True if divisible by both last two digits, False otherwise.
    """
    a = str(num)
    b = int(a[-1])
    c = int(a[-2])
    
    if a[-1] == "0" or a[-2] == "0":
        return False
    else:
        return (num%b == 0) and (num%c == 0)
    
    '''d1 = (num // 10) % 10     # second last digit
    d2 = num % 10             # last digit

    # If any digit is zero → division not allowed → return False
    if d1 == 0 or d2 == 0:
        return False

    # Check divisibility
    return (num % d1 == 0) and (num % d2 == 0)'''