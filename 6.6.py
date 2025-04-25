def modify_tuple(a, index, value):
    t = list(a)
    
    t[index] = value
    modified = tuple(t)
    
    return modified

x = (1, 2, 3, 4)

new = modify_tuple(x, 2, 99)
print("modified tuple:", new)
