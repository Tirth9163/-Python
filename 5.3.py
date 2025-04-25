import random

def dup():
    a = []  
    for _ in range(50):
        m = random.randint(1, 30)
        if m not in a:  
            a.append(m)

    print( sorted(a))

dup()
