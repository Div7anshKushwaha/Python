l = ["fonkey","divya","there","house"]
with open('donkey.txt') as f:
    content = f.read()
for word in l:
    content = content.replace(word,'#'*len(word))    
    
with open('donkey.txt','w') as f:
    f.write(content)
