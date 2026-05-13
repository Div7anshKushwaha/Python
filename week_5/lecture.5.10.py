# LAMBDA FUNCTION

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def mul(x, y):
#     return x * y

# def div(x, y):
#     return x / y

add = lambda x, y: x + y
sub = lambda x, y: x - y      #instesd of using too much functions for a single line we can assign variables as function using lambda function
mul = lambda x, y: x * y
div = lambda x, y: x / y
print (add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))

print(type(add))


#ENUMERATE FUNCTION
fruits = ["mango", "apple", "banana",
"orange", "pineapple", "watermelon", "guava",
"kiwi"]

for fruit in enumerate(fruits): #IT COUPLES INDEX NO. OF EACH ELEMENT WITH ITS ELEMENT TOGETHER IN TUPLE 
    print(fruit)

# ZIP FUNCTION
fruits = ["mango", "apple", "banana",
"orange", "pineapple", "watermelon", "guava",
"kiwi"]
size = [5, 5, 6, 6, 9, 10, 5, 4]

print(dict(zip(fruits, size))) 
print(list(zip(fruits, size)))
print(tuple(zip(fruits, size)))
print(zip(fruits, size))

# MAP FUNCTION


a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]
#c = a + 1
def sub(x, y):
    return x - y
def incr(x):
    return x + 1
c = map(sub, a, b)
c = map(incr, a)
print(list(c))



# FILTER FUNCTIONimport math

import math
a = [25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    if n >= 0:
        return n

c = map(square_root, filter(is_positive, a))   #IT WILL FILTER THE LIST AND TAKE ONLY POSITIVE VALUES FROM THE LIST BASED ON THE FUNCTION ASSIGNED SO THAT IT CAN GIVE THE LIST OF SQUARE ROOTS OF THE LIST a
print(list(c))

















