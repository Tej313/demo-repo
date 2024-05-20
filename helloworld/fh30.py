import os
# Define the path to the directory
directory = '/Users/tej/Desktop/demo/helloworld/helloworld'
# Iterate through the files in the directory
for filename in os.listdir(directory):
    # Check if the file has a .txt extension
    if filename.endswith('.txt'):
        # Open the file in read mode
        with open(os.path.join(directory, filename), 'r') as file:
            # Print the content of the file
            print(file.read())
