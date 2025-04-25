def average(l, i=0, total=0):
    if i == len(l):  
        return total / len(l) 
    return average(l, i + 1, total + l[i])  

x = [int(i) for i in input("Enter numbers: ").split()]  
print(average(x))
