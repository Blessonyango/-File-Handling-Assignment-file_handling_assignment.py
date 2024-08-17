# file_handling_assignment.py

def create_and_write_file(filename):
    try:
        # Creating a new file and writing initial content to it
        with open(filename, 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("And the third line has some more text.\n")
        print(f"File '{filename}' created and initial content written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating or writing to the file: {e}")
    finally:
        print("Finished writing to the file.")

def read_file(filename):
    try:
        # Reading and displaying the content of the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("Finished reading the file.")

def append_to_file(filename):
    try:
        # Appending additional content to the file
        with open(filename, 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("Here is another appended line with number: 67890\n")
            file.write("And one more line for good measure.\n")
        print(f"Additional content appended to '{filename}'.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("Finished appending to the file.")

def main():
    filename = "my_file.txt"
    
    # Step 1: Create and write to the file
    create_and_write_file(filename)
    
    # Step 2: Read and display the file content
    read_file(filename)
    
    # Step 3: Append additional content to the file
    append_to_file(filename)
    
    # Step 4: Read and display the updated file content
    read_file(filename)

if __name__ == "__main__":
    main()
