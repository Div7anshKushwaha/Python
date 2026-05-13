def process_employees(employee_list: list, request: str):
    """
    Process the employee list as per the request.
    
    Args:
        employee_list (list[dict]): List of dictionaries with the keys
            "employee_id", "tasks_completed", and "hours_worked".
        request (str): One of the following options:
            - 'total_tasks_completed'
            - 'most_efficient_employee'
            - 'sort_by_hours_worked'
            - 'productive_team_members'.
        
    Returns:
        The output corresponding to the request.
    """
    if request == "total_tasks_completed":
        count = 0
        for items in employee_list:
            count += items["tasks_completed"]
        return count    
    
    if request == "most_efficient_employee":
        employee = -1
        eff = -1
        task = -1
        for items in employee_list:
            if (items["tasks_completed"]/items["hours_worked"] > eff) or (items["tasks_completed"]/items["hours_worked"] == eff and items["tasks_completed"] > task)  :
                eff = items["tasks_completed"]/items["hours_worked"]
                task = items["tasks_completed"]
                employee = items["employee_id"]
        return employee
    if request == "productive_team_members":
        L = []
        for items in employee_list:
            if items["tasks_completed"]>19:
                L.append(items["employee_id"])
        return L
    
    if request == "sort_by_hours_worked":
        # We will manually sort using selection-sort style logic
        employees = employee_list[:]   # make a copy so original is not changed
        sorted_ids = []

        while employees:
        # pick the employee with maximum hours_worked
        # tie-break with tasks_completed
            best = employees[0]

            for emp in employees[1:]:
                if emp["hours_worked"] > best["hours_worked"]:
                    best = emp
                elif emp["hours_worked"] == best["hours_worked"] and emp["tasks_completed"] > best["tasks_completed"]:
                    best = emp

            sorted_ids.append(best["employee_id"])
            employees.remove(best)

        return sorted_ids
    