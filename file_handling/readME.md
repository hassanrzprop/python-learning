File handling
File handling is a fundamental aspect of Python programming, allowing you to interact with files on your system. Here's an overview:

Key Concepts:

open() function: This function is the gateway to file handling. It takes two arguments: filename and mode. The mode specifies how you want to interact with the file (read, write, append, etc.).
Modes: Common modes include:

r: Read (opens an existing file for reading) w: Write (opens an existing file for writing, overwriting existing data) x: Create (creates a new file, throws an error if the file exists) a: Append (opens an existing file for appending data at the end) r+, w+, a+: Combinations of read/write/append with the ability to move the file pointer File object: When you call open(), it returns a file object, which you use to perform operations on the file. Common methods include:

read(): Reads the entire file content as a string.
readline(): Reads a single line from the file.
readlines(): Reads all lines from the file and returns them as a list.
write(data): Writes data to the file.
close(): Closes the file (important to release resources).
Context manager: The with statement is a convenient way to handle file opening and closing automatically, ensuring the file is closed even if exceptions occur.
file = open("example.txt", "r")  # Opens the file in read mode

# Read the entire content
content = file.read()

# Read a single line
line = file.readline()

# Read all lines into a list
lines = file.readlines()

file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, World!\n")
file.write("This is a new line.\n")
file.close()

file = open("example.txt", "a")  # Opens the file in append mode
file.write("This is appended content.\n")
file.close()


with open("example.txt", "r") as file:
    content = file.read()
    print(content)

