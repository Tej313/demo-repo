import tempfile
# Create a temporary file
with tempfile.TemporaryFile() as temp_file:
    # Write some data to the temporary file
    temp_file.write(b'Some data')
    # Seek to the beginning of the file
    temp_file.seek(0)
    # Read and print the data from the temporary file
    print(temp_file.read())
