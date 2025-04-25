def fibonacci(N):
    a, b = 0, 1  
    count = 0  
    while count < N:
        print(a, end=" ")
        a, b = b, a + b  
        count += 1  

N = int(input("Enter the value of N: "))
fibonacci(N)
