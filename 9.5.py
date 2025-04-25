def ispangram(a):
    alphabet=set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(a.lower())
string=["The quick brown fox jumps over the lazy dog","Crzy Fredrick bought many very exquisite opal jewels"]
for text in string:
    print(ispangram(text))
