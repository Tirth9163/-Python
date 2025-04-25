import os
import shutil

source_dir = input("Enter the source directory path: ")
filename = input("Enter the name of the file to copy: ")
target_dir = input("Enter the target subdirectory name (it will be created): ")



source_file = os.path.join(source_dir, filename)
target_file = os.path.join(target_dir, filename)

if os.path.exists(source_file):
    shutil.copy(source_file, target_file)
    print(f"Copied '{filename}' from '{source_dir}' to '{target_dir}'")
else:
    print(f"Source file '{filename}' not found in '{source_dir}'")
