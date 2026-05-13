#ITERATORS
fruits = ["mango", "apple", "melon", "guava", 
          "orange", "pineapple", "kiwi"]

# for fruit in fruits:       ITERATION IN NOT IN OUR HANDS
#     print(fruit)  

basket = iter(fruits)

print(next(basket))
print(next(basket))
print(next(basket))  #WE CAN ITERATE ANY TIMR ITS ON OUR HANDS
print(next(basket))
print(next(basket))

# GENERATORS (GENERATES ITS OWN ITERATOR)

def square(limit):
    x = 0
    while x < limit:
        yield x * x
        yield x * x * x
        x += 1

a = square(5)
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))
print(next(a), next(a))




