def count(x):
    vowel="aeiouAEIOU"
    i=0
    for char in x:
        if char in vowel:
            i+=1
    print(i)

x=input("enter a string")
count(x)


