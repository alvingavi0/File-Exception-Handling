# error_handling.py

filename = input("Enter the filename you want to open: ")

try:
    # Try opening the file
    with open(filename, "r") as file:
        print("File content:\n")
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
