try:
    f = open("note.txt", "r")
    content = f.read()
    print(content)

except FileNotFoundError:  # if note.txt not exist work this line
    print("File not found.")
finally:
    print("File operation complete.")
