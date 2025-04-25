def compare (a,b):
    if a in b:
        print("first string is present in second")
    elif b in a:
        print("second string is present in first")
    else:
        print("neither is there in other")

x=input("enter first string")
y=input("enter second string")
compare(x,y)
