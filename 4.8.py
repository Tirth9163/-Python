def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

x=int(input("Enter a Number: "))
print("Factorial of",x,"is:",factorial(x))
