import math

def check(x, y, r, p1, p2):
    dis = math.sqrt(pow(p1 - x, 2) + pow(p2 - y, 2))
    
    if dis < r:
        return "point lies inside the circle."
    elif dis == r:
        return "point lies on the circle."
    else:
        return "point lies outside the circle."

x, y = map(float, input("Enter the coordinates of the center of the circle (x y): ").split())
r = float(input("Enter the radius of the circle: "))
p1, p2 = map(float, input("Enter the coordinates of the point (x y): ").split())

result = check(x, y, r, p1, p2)
print(result)
