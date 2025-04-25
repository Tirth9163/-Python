def frequency(s):
    words = s.split()
    d = {}

    for i in words:
        if i in d:
            d[i] += 1  
        else:
            d[i] = 1  

    sorted_dict = dict(sorted(d.items()))  
    return sorted_dict  

x = input("Enter a string: ")
print(frequency(x))
