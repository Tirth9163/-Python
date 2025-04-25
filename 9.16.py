def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

x = int(input("Enter base (a): "))
y = int(input("Enter exponent (b): "))

print(power(x, y))
