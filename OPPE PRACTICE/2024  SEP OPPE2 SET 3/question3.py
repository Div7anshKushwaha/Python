def swap_last_chars_of_values(d: dict, k1, k2):
    """Swap the last chars of the values of given keys in the dict.

    Args:
        d (dict): The dictionary with string values.
        k1: The first key.
        k2: The second key.

    Returns:
        None - modifies the dictionary in-place.
        Examples

Example 1

>>> d = {"first": "apple", "second": "mango", "third":"banana"}
>>> swap_last_chars_of_values(d, "first", "second")
>>> d
{'first': 'applo', 'second': 'mange', "third": "banana"}
    """
    a = d[k1]
    b = d[k2]
    c = a[0:-1] + b[-1]
    dd = b[0:-1] + a[-1]
    d[k1] = c
    d[k2] = dd

