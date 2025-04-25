def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

x = input("Enter a string: ")
print(length(x))
