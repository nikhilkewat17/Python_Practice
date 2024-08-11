import os

# Remove or Delete file .

# Excercise 1: Using remove() method.
os.remove("path")


# Excercise 2: Using if-else statement.
if os.path.exists("path"):
    os.remove("path")
else:
    print("The file does not exists..!")




# Excercise 3: Remove folder using rmdir() method.

os.rmdir("path")

