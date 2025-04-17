# file_rw.py

try:
    # Open the input file to read
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify content (For example, convert it to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File has been successfully modified and saved to output.txt")

except FileNotFoundError:
    print("Error: The input file does not exist.")
