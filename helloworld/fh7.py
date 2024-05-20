from datetime import datetime, timezone  # Import datetime and timezone classes from the datetime module
from os import scandir  # Import scandir function from the os module

def convert_date(timestamp):
    # Convert a POSIX timestamp to a timezone-aware datetime object in UTC
    d = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    # Format the datetime object into a string in the format 'dd MMM YYYY'
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date  # Return the formatted date string

def get_files():
    # Scan the directory 'my_directory/' and get an iterator of DirEntry objects
    dir_entries = scandir('my_directory/')
    for entry in dir_entries:  # Iterate over each entry in the directory
        if entry.is_file():  # Check if the entry is a file
            info = entry.stat()  # Get the status information of the file
            # Print the file name and its last modified date in the desired format
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

# Call the function to list files and their last modified dates in the specified directory
get_files()
