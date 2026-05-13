# nested for loop
s = "VIBGYOR"
t = "VIBGYOR"


count = 0
for i in range(7):
    for j in range(7):
        print(i,j,s[i],s[j])  
        count += 1
print("the total number of ways in which s and t can weat 7 different colours:",count)












