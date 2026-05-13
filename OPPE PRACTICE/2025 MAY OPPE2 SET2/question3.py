def combine_edges(s: str) -> str:
    '''
    Create a new string made of the first two and last two 
    characters from the given string.

    Arguments:
    s: str - a string.

    Return: str - a new string made of the first and last two characters.
    '''
    first = s[0] + s[1]
    last = s[-2] + s[-1]
    string =  first + last
    if len(s)<4:
        return ""
    else:
        return string