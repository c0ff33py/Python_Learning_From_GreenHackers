import os

# check if file exists, then delete
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File deleted.")
else:
    print("File does not exist.")
