# Open file in read mode
f = open("note.txt", "r")

# Read all content
content = f.read()
print("Content of file: ")
print(content)

f.close()
