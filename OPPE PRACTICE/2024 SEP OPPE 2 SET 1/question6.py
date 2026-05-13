def process_grocery_list(grocery_list:list, request:str):
    """Process the grocery list as per the request.

    Args:
        grocery_list (list[dict]) - A list of dictionary with the keys
            "name", "quantity" and "price", where "price" is the amount of 
            one unit of the item.
        request: (str) - A string containing one of the following request.
            - 'total_bill_amount'
            - 'max_quantity_item'
            - 'sort_by_total_amount'

    Returns: 
        The output corresponding to the request.
    """
    if request == "total_bill_amount":
        total = 0
        for items in grocery_list:
            for item in grocery_list:
                # Loop 1: item = {'name': 'apple', 'quantity': 2, 'price': 3}
            # Loop 2: item = {'name': 'banana', 'quantity': 5, 'price': 2}
            # Loop 3: item = {'name': 'carrot', 'quantity': 4, 'price': 1}
                total += item['quantity']*item["price"]
                # Loop 1: total += 2 * 3 → total = 6
                # Loop 2: total += 5 * 2 → total = 6 + 10 = 16
                # Loop 3: total += 4 * 1 → total = 16 + 4 = 20    
        return total 
    elif (request == "max_quantity_item"):
        max_q = -1
        max_name = None
        for item in grocery_list:
            if item['quantity']>max_q:
                max_q = item['quantity']
                max_name = item['name']
        return max_name

    elif request == "sort_by_total_amount":
        # We will use sorted() with a custom key.
        # Key will be:
        #   - primary: negative of total amount (so larger totals come first)
        #   - secondary: name in alphabetical order (for ties)

        return sorted(
            grocery_list,
            key=lambda x: (-(x["quantity"] * x["price"]), x["name"]))
            # For each x (item dict), we compute a tuple:
            # Example items:

            # x = {'name': 'apple', 'quantity': 2, 'price': 3}
            #   total = 2*3 = 6 → key = (-6, 'apple')

            # x = {'name': 'banana', 'quantity': 5, 'price': 2}
            #   total = 10 → key = (-10, 'banana')

            # x = {'name': 'carrot', 'quantity': 4, 'price': 1}
            #   total = 4 → key = (-4, 'carrot')

            # Sorting by these keys:
            # (-10, 'banana')  → biggest total (10) → comes first
            # (-6, 'apple')    → next (6)
            # (-4, 'carrot')   → last (4)

            # Final sorted order:
            # [
            #   {'name': 'banana', 'quantity': 5, 'price': 2},
            #   {'name': 'apple',  'quantity': 2, 'price': 3},
            #   {'name': 'carrot', 'quantity': 4, 'price': 1}
            # ]
        









