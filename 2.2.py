def sort(a,b,c):
    largest = a if a > b and a > c else (b if b > c else c)
    smallest = a if a < b and a < c else (b if b < c else c)
    print("largest is:",largest)
    print("smallest is :",smallest)

x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
sort(x,y,z)
