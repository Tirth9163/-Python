def count(a):
    m = d = 0

    for char in a:
        if ('A'<= char <= 'Z')or('a'<=char<='z'):
            m += 1
        elif '0'<= char <='9':
            d += 1

    print("Alphabets: ",m)
    print("Digits: ",d)

x = input("Enter a string: ")
count(x)
