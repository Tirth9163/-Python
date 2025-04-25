file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
merged_file = input("Enter the name of the output file: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')
f3 = open(merged_file, 'w')

lines1 = f1.readlines()
lines2 = f2.readlines()

max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])

f1.close()
f2.close()
f3.close()

print("Merged content ")
