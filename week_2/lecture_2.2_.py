ram_bank_balance = 100000
# Ram's bank balance, note that this is positive

ram_loan = 50000
# Ram's loan, this is to be returned by him and hence will count as negative

lakshman_bank_balance = 200000
lakshman_loan = 100000

net_income = ram_bank_balance + lakshman_bank_balance
# Net income is the total bank balance of the two brothers

net_liability = ram_loan + lakshman_loan
# Net liability is the total loan of the brothers.

final_value = net_income - net_liability
print("This is the family's final money (could be negative if the family has", final_value)
