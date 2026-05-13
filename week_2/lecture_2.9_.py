# Problem 1
integer = int(input("Enter your number: "))
if(integer%2==0):
    print("The given number is even")
else:
    print("The given number is odd")

# problem 2
integer = int(input("Enter your number: "))
if(integer%5 == 0):
    print("The number ends with 0 or 5")
else:
    print("The number does not ends with 5 or 0")


#problem 3 
marks = int(input("Enter your marks: "))
if(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks< 90):
    print("B")
elif(marks>=70 and marks< 80):
    print("C")
elif(marks>=60 and marks< 70):
    print("D")
elif(marks<60):
    print("E")
else:
    print("Invalid input")


# PROBLEM 4

print("Travel from city A to city B")
time = int(input("Enter time: "))
longer = int(input("Enter Price: "))
if(time>=longer):
    price = int(input("Enter Price: "))
    higher = int(input("Define Higher: "))
    if(price>=higher):
        print("train")
    else:
        print("Coach")
else:
    price = int(input("Enter Price: "))
    higher = int(input("Define Higher: "))
    if(price>=higher):
        print("Daytime flight")
    else:
        print("Red eye flight")
    
print("Arrive City B")






