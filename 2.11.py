def coll(x1,x2,x3,y1,y2,y3):
    if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
        return True
    else:
        return False

x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())

if coll(x1,x2,x3,y1,y2,y3):
    print("points are collinear")
else:
    print("they do not lie on straight line")
