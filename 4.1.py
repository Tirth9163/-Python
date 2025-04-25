def printer():
    print("Uppercase:", end=" ")
    for ch in range(65, 91): 
        print(chr(ch), end=" ")
    
    print("\nLowercase:", end=" ")
    for ch in range(97, 123):  
        print(chr(ch), end=" ")

printer()
