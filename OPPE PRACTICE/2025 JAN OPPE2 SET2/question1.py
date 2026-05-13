def extract_middle_elements(lst:list):
    """
    Extracts the middle element(s) from a list of integers.

    Args:
        lst (list): The list of integers.

    Returns:
        list: A list containing either the middle element (if odd length) or 
        the two middle elements (if even length).
        
    """
    L = []
    l = len(lst)
    if len(lst)%2 == 1:
        L.append(lst[l//2])
    else:
        L.append(lst[l//2 -1])
        L.append(lst[l//2])
    return L
