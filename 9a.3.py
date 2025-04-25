import random  

a = [random.randint(-15, 15) for i in range(10)]  
sqr = [x ** 2 for x in a]  

print("Original List:", a)  
print("Squared List:", sqr)
