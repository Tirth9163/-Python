def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sinx(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1) ** n  
        term = (x ** (2 * n + 1)) / factorial(2 * n + 1) 
        result += sign * term
    return result

degree = float(input("Enter the angle in degree: "))
radian = degree * (3.14159 / 180) 

print(f"sin({degree} degrees) = {sinx(radian)}")
