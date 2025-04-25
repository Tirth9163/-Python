def sum_avg(a1,a2,a3,a4,a5):
    t=a1+a2+a3+a4+a5
    a=t//5
    return t,a
x=[int(i) for i in input("Enter the marks").split()]
print(x)
print(sum_avg(*x))
