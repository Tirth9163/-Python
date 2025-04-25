l1 = input("Enter numbers for first list (space-separated): ").split()
l1 = [int(x) for x in l1]  

l2 = input("Enter numbers for second list (space-separated): ").split()
l2 = [int(x) for x in l2]  
l3 = []
for num in l1:
    if num not in l2:
        l3.append(num)

print("List 1:", l1)
print("List 2:", l2)
print("List 3 :", l3)


