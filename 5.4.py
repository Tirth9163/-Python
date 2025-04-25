import random

def sep():
    a,p,n=[],[],[]
    for i in range(30):
        m = random.randint(-50, 50)
        a.append(m)
    for i in a:
        if i > 0:
            p.append(i)
        elif i < 0:
            n.append(i)

    print("all numbers:", a)
    print("positive numbers:", p)
    print("negative numbers:", n)

sep()
