# LIST MINIPULATION

#1

def list_min(l):
    mini = l[0] 
    for i in range(len(l)):
        if (l[i]<mini):
            mini= l[i]
    return mini
def list_maxi(l):
    maxi = l[0] 
    for i in range(len(l)):
        if (l[i]>maxi):
            maxi = l[i]
    return maxi

def list_appendbefore(l,z):
    newl =[]
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])   
    return newl

def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum +l[i]
        ans = sum/len(l)
    return ans    

l = [1,343,122,-12,453,-145,111]
z = [1,2,3,4,5]
print(list_appendbefore(l,z))
print(list_average(l))
print(list_average(z))
print(list_maxi(l))
print(list_min(l))















