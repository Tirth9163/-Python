from datetime import date
def days(x,y):
    d1=date(x[2],x[1],x[0])
    d2=date(y[2],y[1],y[0])
    return abs ((d2-d1).days)
x=(21,7,2006)
y=(25,11,2005)
print("there are this many days",days(x,y))
