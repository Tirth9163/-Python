input_file = input("Enter the source file name: ")
output_file = input("Enter the output file name: ")

remove_words = {"a", "an", "the"}

with open(input_file, 'r') as f_read:
    lines = f_read.readlines()

with open(output_file, 'w') as f_write:
    for line in lines:
        words = line.split()
        filtered_words = [word for word in words if word.lower() not in remove_words]
        new_line = ' '.join(filtered_words)
        f_write.write(new_line + '\n')

print("Words 'a', 'an', 'the' removed. Output saved in output_file.")
