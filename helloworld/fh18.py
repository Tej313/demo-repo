import os
# Walk through the directory tree starting from the current directory
for dirpath, dirnames, filenames in os.walk('.'):
    # Print the current directory path
    print(f'Found directory: {dirpath}')
    # Iterate through the list of filenames in the current directory
    for file_name in filenames:
        # Print each file name
        print(file_name)
