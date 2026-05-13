def is_arithmetic_progression(sequence: list) -> bool:
    '''
    Given a sequence of numbers, determine if it is an arithmetic progression.

    An arithmetic progression is a sequence where the difference between consecutive terms is constant.

    Examples:
    is_arithmetic_progression([1, 3, 5, 7, 9])
    >>> True
    is_arithmetic_progression([2, 4, 6, 8, 10])
    >>> True
    is_arithmetic_progression([9, 6, 3, 0, -3, -6])
    >>> True
    is_arithmetic_progression([1, 3, 5, 6, 11])
    >>> False
    is_arithmetic_progression([0, 0, 0, 0, 0])
    >>> True
    is_arithmetic_progression([1, 2, 4, 8, 16])
    >>> False

    Args:
        sequence (list): A list of numbers

    Returns:
        bool: True if the sequence is an arithmetic progression, False otherwise
    '''
    # def is_arithmetic_progression(sequence: list) -> bool:
    # A sequence with 0 or 1 element is trivially an AP
    if len(sequence) <= 2:
        return True

    # Compute the common difference using the first two elements
    d = sequence[1] - sequence[0]

    # Check whether all consecutive differences match d
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i - 1] != d:
            return False

    return True
