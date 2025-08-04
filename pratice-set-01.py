# find the word twinkle in your file 


f= open("file-input-output/poem.txt")


show =  f.read()
if("twinkle" in show): 
  print("The word twinkle is present in the content ")
else:
  print("word is not present ")

f.close()
