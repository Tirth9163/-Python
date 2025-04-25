def toggle (a):
    for char in a:
        if 'a' <= char <='z':
             print(chr(ord(char)-32),end ='')
        elif 'A'<= char <='Z':
            print(chr(ord(char)+32),end = '')
x=input("enter a string")
toggle(x)
