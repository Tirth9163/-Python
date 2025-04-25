def create_tuple(a):
    result=[]
    for i in range(1,a+1):
        result.append((x,x**2,x**3))
    return result
x=int(input("Enter a number"))
print(create_tuple(x))
