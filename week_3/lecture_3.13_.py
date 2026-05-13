# BREAK,PASS AND CONTINUE

email = input()
for c in email:
    if(c == '@'):
        break
    print(c,end ='')



email = input()
for c in email:
    if(c == '@'):
        continue
    print(c,end ='')




for i in range(11):
    if(i%3 == 0):
        print(i)
    else:
        pass