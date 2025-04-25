def separater(names):
    a ,b= set(),set()   

    for i in names:
        if i[0]=='A':
            a.add(i)
        elif i[0]=='B':
            b.add(i)

    return a,b

x = {"Alice", "Akshay", "Bobby", "Bhai", "Anand", "Ben", "Anant"}

a,b = separater(x)

print("names starting with A:", a)
print("names starting with B:", b)
