def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))

print(n,"C",r," Combination = ", nCr(n, r))
print(n,"P",r," Permutation = ",nPr(n, r))
