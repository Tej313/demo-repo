import zipfile
import os

# Extract the ZIP file
with zipfile.ZipFile('ir.zip', 'r') as zip_ref:
    zip_ref.extractall('extracted_files')

# Function to list files and directories
def list_files_and_dirs(directory_path):
    for root, dirs, files in os.walk(directory_path):
        print(f'Directory: {root}')
        for file in files:
            print(f'  File: {file}')
        for dir in dirs:
            print(f'  Subdirectory: {dir}')

# List the extracted files and directories
print("Listing files and directories in 'extracted_files':")
list_files_and_dirs('extracted_files')
