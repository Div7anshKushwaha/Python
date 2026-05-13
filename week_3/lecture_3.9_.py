for i in range(10):
    print(i, end=" ") # it will print i and end with space before going to second print



d = 24
m = 1
y = 2007

print("Today\'s date is ",d,m,y,sep = '/') # sep function seperates the , statemets
print("Today\'s date is ",d,m,y,sep = "-") # sep function seperates the , statemets

# # OR 
print("Today's date is ",end = ' ' )
print(d,m,y,sep = '-')


# formatted printing
num = int(input())
for i in range(1,11):
    print(num,"X",i,'=',num*i)
    print(f'{num} X {i} = {num*i}') #everything under {} is considered as variable and everything string
    print('{0} X {1} = {2}'.format(num,i,num*i)) # assign 0 as num, 1 as i , 2 as num*i
    print('%d X %d = %d ' % (num,i,num*i)) # SAME AS 3RD ONE old way of writing print function


# PATTERN PRINTING 1

pi = 22/7
print(f'value of PI = {pi:.3f}')   
print('value of PI = {0:.4f}'.format(pi))
print('value of PI = %.5f' % (pi))

# PATTERN PRINTING 1

print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))


print('{0:5d}'.format(1))      #5d means we need mimimun 5 characters in print statement
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
