def freq (a):
    f={}
    for i in a:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f
x=input("enter a string")
print(freq(x))
