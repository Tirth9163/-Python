def delete(a, index):
    t = list(a)
    
    del t[index]
    
    modified = tuple(t)
    
    return modified

x = (1, 2, 3, 4, 5)

new = delete(x, 1)

print (new)
