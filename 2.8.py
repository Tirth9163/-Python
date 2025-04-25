def triangle(a,b,c):
    if a+b+c==180:
        return True
    else:
        return False

x=int(input("enter an angle:"))
y=int(input("enter an angle:"))
z=int(input("enter an angle:"))

if triangle(x,y,z):
    print("the triangle is valid")
else:
    print("triangle is not valid")
