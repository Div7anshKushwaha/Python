def is_reverse_combined_palindrome(s1: str, s2: str) -> str:
    '''
    Given two strings, 
    - Reverses the first string
    - Concatenates it with the second string
    - Checks if the result is a palindrome or not

    Examples:
    >>> is_reverse_combined_palindrome("mad", "am")
    False
    >>> is_reverse_combined_palindrome("dam", "am")
    True

    Args:
        s1 (string): The first string
        s2 (string): The second string

    Returns:
        str : check the palindrome or not
    '''
    a1 = s1[::-1]
    string = a1+s2
    
    if string == string[::-1]:
        return True
    else:
        return False