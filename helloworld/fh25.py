import zipfile
# Create a new ZIP file named 'new_archive.zip'
with zipfile.ZipFile('ir.zip', 'w') as zip_ref:
    # Add a file named 'file_to_add.txt' to the ZIP archive
    zip_ref.write('file_to_add.txt')
