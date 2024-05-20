import json  # Import the json module for working with JSON data.
import requests  # Import the requests library for making HTTP requests.

# Fetch TODO data from the API
response = requests.get("https://jsonplaceholder.typicode.com/todos")  # Make a GET request to fetch TODO data from the JSONPlaceholder API.
todos = json.loads(response.text)  # Deserialize the response text into a Python list representing TODO items.

# Analyze the TODO data
todos_by_user = {}  # Create an empty dictionary to store the number of completed TODOs for each user.
for todo in todos:  # Iterate over each TODO item in the list.
    if todo["completed"]:  # Check if the TODO item is completed.
        if todo["userId"] in todos_by_user:  # Check if the user ID already exists in the dictionary.
            todos_by_user[todo["userId"]] += 1  # Increment the count of completed TODOs for the user.
        else:
            todos_by_user[todo["userId"]] = 1  # Initialize the count of completed TODOs for the user to 1.

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)  # Sort the dictionary by the number of completed TODOs in descending order.
max_complete = top_users[0][1]  # Get the number of completed TODOs for the user with the highest count.
users = [str(user) for user, num_complete in top_users if num_complete == max_complete]  # Extract the user IDs with the highest count of completed TODOs.
max_users = " and ".join(users)  # Join the user IDs into a single string.

# Write filtered TODOs to file
def keep(todo):  # Define a function to filter TODO items based on completion status and user ID.
    is_complete = todo["completed"]  # Check if the TODO item is completed.
    has_max_count = str(todo["userId"]) in users  # Check if the user ID matches the users with the highest count of completed TODOs.
    return is_complete and has_max_count  # Return True if the TODO item is completed and belongs to a user with the highest count.

filtered_todos = list(filter(keep, todos))  # Filter the TODO items based on the defined criteria.
with open("filtered_data_file.json", "w") as data_file:  # Open a file to write the filtered TODOs.
    json.dump(filtered_todos, data_file, indent=2)  # Serialize the filtered TODOs and write them to the file with indentation for readability.

print(f"user{'s' if len(users) > 1 else ''} {max_users} completed {max_complete} TODOs")  # Print a summary of the users with the highest count of completed TODOs.
