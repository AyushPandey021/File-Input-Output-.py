st= ".Hey Ayush You are amazing "
f = open("file-input-output/my.md", "a") #a for append
# use append to insert the st line. and if you run many time so its add many time in file 
f.write(st)
print(st)

f.close()

