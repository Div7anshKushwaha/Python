def greatest_of_three(a,b,c):
    if a>b>c:
        return a
    elif b>a>c:
        return b
    else:
        return c
print(greatest_of_three(2,5,7))  
