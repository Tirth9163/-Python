def sanitize(l, i=0):
    if i == len(l):
        return l
    if l[i] < 0:
        l[i] = 0
    return sanitize(l, i + 1)

x = [int(i) for i in input("Enter numbers: ").split()]
print(sanitize(x))
