def compute_electricity_bill(units: int) -> float:
    """
    Calculate the electricity bill.

    - <=200 units : 0.5 per unit
    - <= 400 units : 0.75 per unit + 150 extra
    - > 400 units : 0.90 per unit + 300 extra

    Args:
        units (int): Number of units consumed.

    Returns:
        float: Total amount to be paid.
    """
    if units <= 200:
        return units * 0.5
    
    elif units <= 400:
        return units * 0.75 + 150
    
    else:  # units > 400
        return units * 0.90 + 300
