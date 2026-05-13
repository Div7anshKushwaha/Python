#1
l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12,l21)
#2
L1 =  [0,0,0,0,0,0,0,0,0,0]
L2= [0]*10
print(L2,L1)

a1 = [1,2,3]*5
print(a1)

#3
print([1,2]<[2,1])
print([1]<[1,2,3])
print([2,3]<[3])   
print([]<[1])


#4
k1 = [2,4,6]
print(k1)
k1[2]= 3
print(k1)  #Lists are mutable ,string is immutale

#5
x = 5
y = x 
x = 10
print(x,y)

c1 = [1,2,3]
c2 = c1
c1[0] = 100
print(c1,c2)

#6

def add(x):
    x.append(1)
    return x

x = [5]
print(add(x))
print(x)


#7 LIST METHODS

k1 = [1,2,3]
print(k1)

k1.append(4)
print(k1)

k1.insert(2,9)
print(k1)

k1.remove(2)
print(k1)

k1.pop(0)
print(k1)


k1.sort()
print(k1)


k1.reverse()
print(k1)


