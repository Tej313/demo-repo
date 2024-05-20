import tarfile
# Create a new TAR file named 'new_archive.tar.gz'
with tarfile.open('new_archive.tar.gz', 'w:gz') as tar_ref:
    # Add a file named 'file_to_add.txt' to the TAR archive
    tar_ref.add('file_to_add.txt')
