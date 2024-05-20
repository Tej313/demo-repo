# List of file names
files = ['file1.txt', 'file2.py', 'file3.txt']
# Filter the list to include only .txt files
txt_files = [file for file in files if file.endswith('.txt')]
# Print the filtered list
print(txt_files)
