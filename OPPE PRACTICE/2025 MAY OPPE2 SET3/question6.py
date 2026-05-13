def book_analysis(data: list, request: str):
    """
    Perform the operation specified by ``request`` on the list of book dictionaries ``data``.

    Supported requests:
    - "average_rating"
    - "average_pages"
    - "longest_book"
    - "above_average_books"
    """
    if request == "average_rating":
        avg = 0
        for entry in data:
            avg+= entry["rating"]
            
        return round(avg/len(data),2)
        
    if request == "average_pages":
        avg = 0
        for entry in data:
            avg += entry["pages"]
        return round(avg/len(data),2)
        


    if request == "longest_book":
        max_pages = -1
        max_rating = -1
        best_id = None

        for book in data:
            pages = book["pages"]
            rating = book["rating"]

            if pages > max_pages:
                max_pages = pages
                max_rating = rating
                best_id = book["book_id"]

            elif pages == max_pages and rating > max_rating:
                max_rating = rating
                best_id = book["book_id"]

        return best_id
    if request == "above_average_books":
        avg = 0
        rating = 0
        realavg = 0
        realrating = 0
        for entry in data:
            avg += entry["pages"]
            rating += entry["rating"]
        avg = avg/len(data)
        rating = rating/len(data)
        result = set()
        for book in data:
            if book["rating"]> rating and book["pages"]>avg:
                result.add(book["book_id"])
                
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        