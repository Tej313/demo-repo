import tarfile
import os

# Function to list files and directories
def list_files_and_dirs(directory_path):
    for root, dirs, files in os.walk(directory_path):
        print(f'Directory: {root}')
        for file in files:
            print(f'  File: {file}')
        for dir in dirs:
            print(f'  Subdirectory: {dir}')

# Open a TAR file named 'sum.tar.gz'
with tarfile.open('sum.tar.gz', 'r:gz') as tar_ref:
    # Extract all the contents of the TAR file to the 'extracted_files' directory
    tar_ref.extractall('extracted_files')

print("Extraction complete. Listing extracted files and directories:")

# List the extracted files and directories
list_files_and_dirs('extracted_files')

