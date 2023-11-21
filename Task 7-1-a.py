import datetime

def create_test_file():
    try:
        # Get the current timestamp
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Create a file with the timestamp as its name
        file_name = f"test_file_{current_timestamp}.txt"
        with open(file_name, 'w') as file:
            file.write("This is a test file.")

        print(f"Test file '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create the test file
create_test_file()
