def read_and_display_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# for Example :
file_name = 'file_with_timestamp.txt'  # here is my text file
read_and_display_file(file_name)
