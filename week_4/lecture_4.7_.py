#List comprehensions
a = 10 
b = 20 

'''
if a < b:
    small = a
else:
    small = b

print(small)
'''

small = a if a<b else b
print(small)


#2 
a = 5 
'''
while a > 0:
    a-= 1
    print(a)
'''
while a>0: print(a); a -= 1

#3
fruits = ["mango","apple","banan","guava","orange","pineapple","watermelon","kiwi"]

newlist = [fruits.capitalize() for fruits in fruits if "n" in fruits]
print(newlist)

'''
newlist = []
for fruits in fruits:
    if "n" in fruits:
       newlist.append(fruits.capitalize())
print(newlist)
'''


