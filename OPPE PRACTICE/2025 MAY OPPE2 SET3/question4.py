def count_special(words):
    """
    Counts how many words in the given list have the same first and last
    characters (case-insensitive) but different second and secondlast
    characters (also case-insensitive).

    Args:
        words (list of str): List of words to examine.

    Returns:
        int: Number of words satisfying the conditions.

    Examples:
        >>> count_special(["Bulb", "deed", "civic", "Noon"])
        1
        >>> count_special(["abca", "aXba", "xyzzyx", "abcaXab"])
        2
    """
    count = 0
    for word in words:
        if (word[0].lower() == word[-1].lower()) and (word[1].lower() != word[-2].lower()):
            count += 1
    return count
    
