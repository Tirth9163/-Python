source_file = input("Enter the source file name: ")
target_file = input("Enter the target file name: ")

f_read = open(source_file, 'r')
content = f_read.read()
f_read.close()

content_upper = content.upper()

f_write = open(target_file, 'w')
f_write.write(content_upper)
f_write.close()

print("copied with converting lowercase to uppercase")
