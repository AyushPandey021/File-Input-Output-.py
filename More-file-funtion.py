f = open("file-input-output/ok.md")
all_Lines = f.readlines()  # all text of text file
# line1 = f.readline()  # line 1 only print
# line2 = f.readline()  # line 2 is only print
# line3 = f.readline()  # line 3 is only print

# # readline for reading one line
# # readlines for multiple lines

# print(line1, type(line1))
# print(line2, type(line2))
# print(line3, type(line3))
# print(all_Lines, type(all_Lines))

# f.close()

# # same thing are doing with loop
# line = f.readline()

while(all_Lines !=""):
    print(all_Lines)

    all_Lines= f.readline()
