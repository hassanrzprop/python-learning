# pen() function: This function is the gateway to file handling. It takes two arguments: filename and mode. The mode specifies how you want to interact with the file (read, write, append, etc.).
# 1)r: Read (opens an existing file for reading) w: Write (opens an existing file for writing, overwriting existing data)
# 2)x: Create (creates a new file, throws an error if the file exists)
# 3)a: Append (opens an existing file for appending data at the end)
# 4)r+, w+, a+: Combinations of read/write/append with the ability to move the file pointer File object: When you call open(), it returns a file object, which you use to perform operations on the file
try:
    file = open("F:/Learning PYTHON/PYTHON-NaveedSarwar/file_handling/exam.txt", "r")
except Exception as e:
    print("ERROR:", e)
else:
    content = file.read()
    readSingleLine=file.readline()
    readAllLines=file.readlines()
    print(content)
finally:
    file.close()


#1)      read(): Reads the entire file content as a string.
#2)      readline(): Reads a single line from the file.
#3)      readlines(): Reads all lines from the file and returns them as a list.
#4)      write(data): Writes data to the file.
#5)      close(): Closes the file (important to release resources).
#6)      Context manager: The with statement is a convenient way to handle file opening and closing automatically, ensuring the file is closed even if exceptions occur.

file1=open("F:/Learning PYTHON/PYTHON-NaveedSarwar/file_handling/exam.txt","a")
file1.write("this a text written by python file using file \nhandling")
file2=open("F:/Learning PYTHON/PYTHON-NaveedSarwar/file_handling/exam.txt","r")
content2=file2.read()
print(content2)