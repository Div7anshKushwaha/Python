# INTRO TO FUNCTIONS
def add(a,b):
    ans = a+b
    print(ans)
add(12,112)    

def discount(cost,d):
    ans = cost-cost*(d/100)
    print(ans)

discount(100,10)

add(10,10) + discount(100,10) #GIVES ERROR

def discount(cost,d):
    ans = cost-cost*(d/100)
    return ans
c = int(input("Enter the cost price: "))
d = int(input("Enter the discount: "))
print("THE final discount is" , discount(c,d))







