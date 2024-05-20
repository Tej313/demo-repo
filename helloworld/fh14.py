import re
# List of file names
files = ['file1.txt', 'file2.py', 'file3.txt']
# Compile a regular expression pattern to match files with names like 'fileN.txt'
pattern = re.compile(r'file\d+\.txt')
# Filter the list using the compiled pattern
txt_files = [file for file in files if pattern.match(file)]
# Print the filtered list
print(txt_files)
