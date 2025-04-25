def triplet(l):
    for a in range(1, l + 1):
        for b in range(a, l + 1):  
            c = (a**2 + b**2)**0.5  
            if int(c) == c and c <= l:  
                print(a, b, int(c))  

l = 30
triplet(l)
