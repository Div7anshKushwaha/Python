# TUPLES (immutable)
#1
t = 1,2,3
print(t,type(t))

x,y,z = t
print(x,y,z)

x = 5 
y = 10
x,y = y,x 
print(x,y)
#2
l = [10]
print(l,type(l))

q = (10)
p = (10,)
print(t,type(q),type(p))  #python consider single element as integer if we didn't use comma(,)

#3
a = ([2,3],["a","b"])

a[0][0] = 10 # we cannot change tuples but the elements inside element of tuple can be changed
print(a)

t1 = (1,2,3) #HASHABLE if the values inside tuples are also immutale then the tuple is considered as hashable
t2 = ([1,2,3],)  #NOT HASHABLE if values inside tuple are mutable then tuple is referred as non-hashable












