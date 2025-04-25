def compute(a):
    n1=int(str(a))
    n2=int(str(a)*2)
    n3=int(str(a)*3)
    n4=int(str(a)*4)
    return n1+n2+n3+n4
for i in range(4,8):
    print("computing:",i,compute(i))
