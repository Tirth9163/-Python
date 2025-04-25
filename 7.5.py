def bill(a,b):
    t=0
    for i in a:
        if i in b:
            t+=(a[i]*b[i])
    return t
x={"Milk":100,"potatoes":30,"onion":40}
y={"Milk":2,"sauce":1,"potatoes":1,"onion":2}

print(bill(x,y))
