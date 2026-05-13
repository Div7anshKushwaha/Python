ram_bank_balance = 100000
#ram's bank balance,note thath this is positive
ram_loan = 500000
#ram's loan note that it is negative because it is to be returned


lakshman_bank_balance = 200000
lakshman_loan = 1000000
net_income=ram_bank_balance+lakshman_bank_balance
# net income is the total bank balance of the brothers
net_liability=ram_loan+lakshman_loan
# net liability is the total loan of the brothers
final_liability=net_income-net_liability
#final income is the family's final monry (could be =ve or -ve)
print("So the family has",final_liability)
