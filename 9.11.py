def create_list(a, b):
    l = []

    for i in a:
        if i in b and i not in l:
            l.append(i)

    return l

x = [int(i) for i in input("Enter elements of first list: ").split()]
y = [int(i) for i in input("Enter elements of second list: ").split()]

print(create_list(x, y))
