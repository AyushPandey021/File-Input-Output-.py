word =[ "Donkey","good","motivated"]

with open("file-input-output/Donkey.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "#"*len(word))

with open("file-input-output/Donkey.txt", "w") as f:
    f.write(contentNew)

