def count_vowels(s, i=0):
    v = "aeiouAEIOU"

    if i == len(s):  
        return 0  

    if s[i] in v:  
        return 1 + count_vowels(s, i + 1)  
    else:  
        return count_vowels(s, i + 1)  

x = input("Enter a string: ")
print(count_vowels(x))
