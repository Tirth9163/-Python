def reverser(a):
    if len(a) <= 1:
        return a
    return [a[-1]] + reverser(a[:-1])

x = [int(i) for i in input("Enter numbers: ").split()]
print(reverser(x))
