def prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def perfect(a):
    n = 0  
    for i in range(1, a):  
        if a % i == 0:  
            n += i 
    return n == a

def armstrong(a):
    num = str(a)         
    power = len(num)     
    total = 0  
    
    for digit in num:
        total += int(digit) ** power  
    return total == a 

def palindrome(a):
    return str(a) == str(a)[::-1]

def automorphic(a):
    square = a ** 2
    return str(square).endswith(str(a))

x = int(input("Enter a number: "))

print(f"{x} is Prime" if prime(x) else f"{x} is not Prime")
print(f"{x} is Perfect" if perfect(x) else f"{x} is not Perfect")
print(f"{x} is Armstrong" if armstrong(x) else f"{x} is not Armstrong")
print(f"{x} is Palindrome" if palindrome(x) else f"{x} is not Palindrome")
print(f"{x} is Automorphic" if automorphic(x) else f"{x} is not Automorphic")
