def cleaner(a):
    clean = []
    
    for item in a:
        if item:  
            clean.append(item)
    
    return clean

x = [(), (1, 2), (), (3, 4), (), (5, 6)]
print(x)
l = cleaner(x)
print(l)
