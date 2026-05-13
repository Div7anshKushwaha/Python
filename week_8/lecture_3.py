f = open('directory.txt', 'r')

flag = 0
s = '0'

while s != '':
    s = f.readline()    # READS EACH LINE IN THE FILE
    if s != '':
        n = int(s)
        if n == 9989591558:
            print("The number was found")
            flag = 1
            break

if flag == 0:
    print("The number was NOTTTT found")

# s = f.readline()
# print(s)
# s = f.readline()
# print(s)
# s = f.readline()      WHEN THE FILE END IT WILL PRINT: '' 
# print(s)
# s = f.readline()      NO MATTER HOW BIG THE FILE IS IF YOU READ IT LINE BY LINE IT WILL NEVER CRASH TO OPEN OR TAKE TIME TO READ LINE
# print(s)
# s = f.readline()
# print(s)
# s = f.readline()
# print(s)
# s = f.readline()
# print(s)
# s = f.readline()
# print(s)