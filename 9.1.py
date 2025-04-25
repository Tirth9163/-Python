def count_lower_upper(a):
    d={"uppercase":0,"lowercase":0}
    for i in a:
        if i.isupper():
            d["uppercase"]+=1
        elif i.islower():
            d["lowercase"]+=1
    return d
x=input("Enter a string")
print(count_lower_upper(x))
