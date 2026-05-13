def product_of_sum_and_abs_diff_of_digits(num: int):
    """Returns the product of the sum and absolute difference of digits of a two digit number.

    Assume number is a two digit number.

    Args:
        num (int) - The given number

    Returns:
        The required product.

    Examples:
        >>> product_of_sum_and_abs_diff_of_digits(38)
        55
        >>> product_of_sum_and_abs_diff_of_digits(55)
        0
    """
    a = str(num)
    b = int(a[0])
    c = int(a[1])

    sum = c + b 
    diff = abs(c-b)
    return sum*diff
    
    '''
    # Extract the two digits
    d1 = num // 10       # tens digit
    d2 = num % 10        # ones digit

    # Compute sum of digits
    s = d1 + d2

    # Compute absolute difference
    diff = abs(d1 - d2)

    # Return product
    return s * diff
    '''