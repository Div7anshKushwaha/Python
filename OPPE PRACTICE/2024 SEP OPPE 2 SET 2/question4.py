def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    """
    Counts the number of vowels and consonants at even indices in the given string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing two integers:
            - The first integer is the count of vowels at even indices.
            - The second integer is the count of consonants at even indices.

    Example:
        >>> count_vowels_and_consonants_in_even_indices("example1")
        (3, 1)

        >>> count_vowels_and_consonants_in_even_indices("hello")
        (1, 2)
    """
    # def count_vowels_and_consonants_in_even_indices(s: str):

    vowels = "aeiouAEIOU"
    vcount = 0
    ccount = 0

    for char in s[0::2]:       # even indices
        if char.isalpha():     # only letters
            if char in vowels:
                vcount += 1
            else:
                ccount += 1

    return (vcount, ccount)