import zipfile
# Open a password-protected ZIP file named 'protected_archive.zip'
with zipfile.ZipFile('ir.zip', 'r') as zip_ref:
    # Extract all the contents of the ZIP file to the 'extracted_files' directory using the provided password
    zip_ref.extractall('extracted_files', pwd=b'password')
