def transfer_amount(accounts, sender, recipient, amount):
    '''
    Performs a transaction between two accounts if the transaction is valid.

    Args:
        accounts (dict): A dictionary of account numbers and their respective balances.
        sender (str): The account number of the sender.
        recipient (str): The account number of the recipient.
        amount (int): The amount to be transferred.

    Returns:
        None - this updates the dictionary accordingly.
    '''
# def transfer_amount(accounts: dict, sender: str, recipient: str, amount: int):
    
    # Lambda function to check transfer validity
    is_valid = lambda: (
        sender in accounts and
        recipient in accounts and
        amount >= 0 and
        accounts[sender] >= amount
    )
    
    # If valid, do the transfer
    if is_valid():
        accounts[sender] -= amount
        accounts[recipient] += amount
