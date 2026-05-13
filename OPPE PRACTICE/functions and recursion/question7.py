def function(list,divya):
    L = []
    for items in list:
        if items != "divya":
            L.append(items.strip(divya))
    return L

print(function(["raj","divya","divyansh","divyanshi",],"divya"))