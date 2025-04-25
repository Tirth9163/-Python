def convert(s):
    words = s.split()  
    u = list(set(words))  
    s = sorted(u)  
    return " ".join(s)  

x = input("Enter a string: ")
print(convert(x))
