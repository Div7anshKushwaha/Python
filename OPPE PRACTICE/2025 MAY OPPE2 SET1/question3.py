def is_pangram(text: str) -> bool:
    '''
    Given a string, check if it is a pangram (contains all letters of the alphabet at least once).

    Examples:
    >>> is_pangram("the quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("this is not a pangram")
    False
    >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
    True 
    >>> is_pangram("zyxwvutsrqponmlkjihgfedcba")
    True 

    Args:
        text (str): The input string

    Returns:
        bool: True if the string is a pangram, False otherwise
    '''
    
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for char in alpha:
        if char not in text:
            return False

    return True
 