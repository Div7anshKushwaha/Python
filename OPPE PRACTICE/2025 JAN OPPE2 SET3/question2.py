def absolute_time_difference(time1, time2):
    """
    Calculates the absolute time difference between two given times in the format HH:MM.

    Args:
        time1 (str): The first time in the format HH:MM.
        time2 (str): The second time in the format HH:MM.

    Returns:
        str: The absolute time difference between the two input times in the format HH:MM.

    Examples:
        >>> absolute_time_difference('14:30', '06:45')
        '07:45'
        >>> absolute_time_difference('06:45', '14:30')
        '07:45'
        >>> absolute_time_difference('23:59', '00:00')
        '23:59'
    """
# def absolute_time_difference(time1, time2):
    # extract hours and minutes using slicing
    h1 = int(time1[:2])
    m1 = int(time1[3:])
    h2 = int(time2[:2])
    m2 = int(time2[3:])
    
    # convert both times to total minutes
    total1 = h1 * 60 + m1
    total2 = h2 * 60 + m2
    
    # absolute difference
    diff = abs(total1 - total2)
    
    # convert back to hours and minutes
    hours = diff // 60
    mins = diff % 60
    
    # return formatted HH:MM
    return f"{hours:02d}:{mins:02d}"
    # return str(hours) + ":" + str(mins)