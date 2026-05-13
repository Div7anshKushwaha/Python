# Write your code here
n = int(input().strip())

L = []
for _ in range(n):
    s = input().strip().split()
    
    first = s[-1]
    second = s[:-1]
    p = ""
    for ch in second:
        p += ch[0]+ "."
        
    L.append(first+ ", " + p)    
L.sort()  
for items in L:
    print(items)