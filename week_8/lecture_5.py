#CAESAR CIPHER

'''This program considers an input file and encrypts it by using caesar cipher. 
By that we mean, we shift the letters by 3 units. 
For example, a becomes d, b becomes e and so on... w becomes z, 
x becomes a, y becomes b and z becomes c'''

import string

def create_caesar_dictionary():
    l = string.ascii_lowercase
    l = list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i + 3) % 26]
    return d

f = open('sherlock.txt', 'r')
g = open('encrypted_sherlock.txt', 'w')
d = create_caesar_dictionary()

c = f.read(1)     #READS ONLY THE Nth LETTER INSIDE THE BRACKET(N) 
while (c != ''):
    g.write(d[c])
    c = f.read(1)
f.close()
g.close()




'''Try writing a code which takes encrypted_sherlock. txt as an
input file and decrypts it and gets back your sherlock. txt'''















