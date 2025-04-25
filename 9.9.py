def count_alpha_digits(a):
    d = {"alphabets": 0, "digits": 0}

    for i in a:
        if i.isalpha():
            d["alphabets"] += 1
        elif i.isdigit():
            d["digits"] += 1

    return d

x = input("Enter a string: ")
print(count_alpha_digits(x))
