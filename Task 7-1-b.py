import datetime

def create_file_with_timestamp():
    try:
        # Get the current timestamp
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a file with the timestamp as its name
        file_name = f"file_with_timestamp.txt"
        with open(file_name, 'w') as file:
            file.write(f"Content generated at {current_timestamp}.")

        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create the file with the current timestamp as content
create_file_with_timestamp()
