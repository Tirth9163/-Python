def grade(marks):
    if marks == -1:  
        return "NA"
    elif marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    else:
        return "O"

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
    
if sub1 <= 39 or sub2 <= 39 or sub3 <= 39:
        status = "Fail"
else:
        status = "Pass"
    
total = sub1 + sub2 + sub3
avg = total/ 3
    
print("Total Marks:",total)
print("Average Marks: ",avg)
print("Pass/Fail: ",status)
    
print("Grade for Subject 1: ",grade(sub1))
print("Grade for Subject 2: ",grade(sub2))
print("Grade for Subject 3: ",grade(sub3))
