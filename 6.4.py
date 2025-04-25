def sorter(a):  
    fl = sorted(a, key=lambda x: x[1], reverse=True)  
    return fl  

x = [("paneer", 120), ("pizza", 250), ("pasta", 180), ("fries", 90), ]  
sf = sorter(x)  

for item, price in sf:  
    print(item ,price)  
