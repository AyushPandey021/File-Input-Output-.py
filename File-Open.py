"""how to read file and open it 
close 
append 
delete 
understanding how to read file path"""

"""
a = "a very long string with emails
email = []
3 second
"""

"""
Understanding one thing⏭️
The random-access is volatile and all its contents are lost once a program terminates in order to persist the data forever we use files.
but but a file data stored devicee a python pragram can talk to the file by reading 
content from it and writeing content to it .
 Not using Volatile memory = RAM 
 use HDD - non Volatile (like Hard disk)
"""
f = open("file-input-output/ok.md")
# open use for opening file write open and (filePath)
data = f.read()
print(data)
f.close()  # its improtant to your file other wise his given problem
# ⏭️you have a 2 type of file 1.Textfile= txt,md file , 2.BinaryFile(jpg,.dat etc) ⏭️


# ⭐2nd mathod if you open the file but not closed so its possible. you only open file and dont bi right f.close() as well⭐
with open("file-input-output/my.md") as f:
    print(f.read())

#  you dont have explicitly close the file
