def table(a):
    print("multiplication table of ",a)
    for i in range(1, 11):  
        print(a,"*",i,"=",a*i)

x = int(input("Enter a number: "))
table(x)
