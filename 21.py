gross = float(input("Enter the number of gross salary: "))

allowance=gross*0.1
deduction=gross*0.03
net= gross+allowance-deduction

print("Number of net salary is",net)
