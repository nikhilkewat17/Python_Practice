# 4. File Backup:
#    Write a Python program that copies the contents of one file to another file,
# creating a backup of the original file.



# Read content from the source file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice.txt", "r") as source:
    content = source.read()

# Write content to the backup file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Backup_Practice.txt" , "a") as backup:
    backup.write(content)

print("Backup created successfully!")


