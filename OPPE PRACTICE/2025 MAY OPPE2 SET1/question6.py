def get_short_books(book_data:list) -> set:
    """Returns the list of ISBNs of the books with pages less than 200."""

    L1 = set()
    for items in book_data:
        if items[1] < 200:   # pages < 200
            L1.add(items[0]) # add isbn
    return L1



def get_medium_books(book_data:list) -> set:
    """Returns the list of isbns of the books with pages Between 200 and 500(inclusive)."""
    L1 = set()
    for items in book_data:
        if 200<= items[1] <= 500:   # pages < 200
            L1.add(items[0]) # add isbn
    return L1
    

def get_pages_by_isbn(book_data:list, isbn: str) -> int:
    """Returns the number of pages in the book given the ISBN."""
    for items in book_data:
        if isbn == items[0]:
            return items[1]
    

def count_by_language(book_data:list) -> dict:
    """Returns a dict with the languages as keys and the number of books of that language as values."""

    counts = {}

    for item in book_data:
        lang = item[2]   # language is stored at index 2

        if lang in counts:
            counts[lang] += 1
        else:
            counts[lang] = 1

    return counts

        
    
    

def total_pages_in_genre_lang(book_data:list, genre:str, lang:str) -> int:
    """Returns the total number of pages from all the books with the given genre and language."""
    pages = 0
    for items in book_data:
        if genre == items[3] and lang == items[2]:
            pages += items[1]
            
    return pages
