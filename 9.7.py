def ispalindrome(a):
    a = a.replace(" ", "").lower()
    return a == a[::-1]

x = input("Enter a string: ")
if ispalindrome(x):
    print("palindrome")
else:
    print("not a palindrome.")
