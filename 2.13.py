def convert(a):
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen"
    ]
    
    if 0 <= a <= 19:
        return words[a]
    else:
        return "Number out of range"


x = int(input("Enter a number between 0 and 19: "))
word = convert(x)
print("The number  in words is: ",word)
