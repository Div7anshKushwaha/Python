#WRITING MODE IN FILES
f = open('mytext.txt','w')
f.write("Divyanshh ")
f.write("Kushwaha ")
f.write("is my name and ")
f.write("I am a data science student ")
f.write("from IIT Madras")
f.close()



#READING MODE IN FILES
x = open('mytext.txt','r')
print(x.read())



#WRITING NEXT LINE IN FILE
g = open('newfile.txt','w')
# g.write('this is the first line')
# g.write("this is the second line")
# output == this is the first linethis is the second line

g.write('this is the first line')
g.write('\n')
g.write("this is the second linee")
g.close()
# output == this is the girst line
#           this is the second line

y = open('newfile.txt','r')
print(y.read())







