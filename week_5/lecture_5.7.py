# Scope of variables 
# Difference between local and global variables

def myFunction1(x):
    x = x * 2                             #TAKING THIS AS LOCAL VARIABLE
    print("Value of x in function 1", x)

def myFunction2(x):
    x = x * 3                               #TAKING THIS AS LOCAL VARIABLE
    print("Value of x in function 2", x)

x = 5                                         #TAKING THIS AS GLOBAL VARIABLE
print("Value of x before function call", x)
myFunction1(x)
myFunction2(x)
print("Value of x after function call", x)

print("Done")
# GLOBAL VARIABLE

def myFunction1():
    global x                                #MADE THIS AS GLOBAL VARIABLE
    x = x * 2
    print("Value of x in function 1", x)

def myFunction2():
    global x                                     #MADE THIS AS GLOBAL VARIABLE
    x = x * 3
    print("Value of x in function 2", x)

x = 5                                          #ALREADY A GLOBAL VARIABLE
print("Value of x before function call", x)
myFunction1()
myFunction2()
print("Value of x after function call", x)

# THIS WILL GIVE ERROR

# def myFunction1():
#     x = x * 2                             #TAKING THIS AS LOCAL VARIABLE
#     print("Value of x in function 1", x)

# def myFunction2():
#     x = x * 3                               #TAKING THIS AS LOCAL VARIABLE
#     print("Value of x in function 2", x)

# x = 5                                         #TAKING THIS AS GLOBAL VARIABLE
# print("Value of x before function call", x)
# myFunction1()
# myFunction2()
# print("Value of x after function call", x)





