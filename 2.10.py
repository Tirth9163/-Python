def compare(a,b):
    area=a*b
    per=2*(a+b)

    if area>per:
        return True
    else:
        return False

l=float(input("Enter lenghth of rectangle"))
b=float(input("Enter breadth of rectangle"))

if compare(l,b):
        print("area of rectangle is greater than its perimeter")
else:
    print("area is not greater than its perimeter")
