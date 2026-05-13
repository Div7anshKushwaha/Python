with open('pythn.txt') as f:
    lines = f.readlines()



lineno = 1
for line in lines:
    if ("python" in line):
        print(f"yes python is present and the line no. is {lineno}")
        break
    lineno += 1
else:
    print("No python is not present ")





