import fnmatch
# List of file names
files = ['file1.txt', 'file2.py', 'file3.txt']
# Use fnmatch to filter the list to include only .txt files
txt_files = fnmatch.filter(files, '*.txt')
# Print the filtered list
print(txt_files)
