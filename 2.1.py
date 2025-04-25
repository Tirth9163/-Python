def sort(a,b):
    if a>b:
     print("largest number is ",a)
     print("smallest  number is",b)
    elif a==b:
     print("both are same")
    else:
     print("largest number is ",b)
     print("smallest  number is",a)

x=int(input("enter first number:"))
y=int(input("enter second number:"))
sort(x,y)
