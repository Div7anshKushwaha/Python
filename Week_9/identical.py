with open('this.txt') as f:
    a = f.read()


with open('copiedtest.txt') as g:
    b = g.read()    


if a == b:
    print("TRUE")    
else:
    print("FALSE")    