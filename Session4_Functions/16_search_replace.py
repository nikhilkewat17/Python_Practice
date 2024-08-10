# 5. File Search and Replace:
#    Write a Python program that reads a text file, searches for a specific string
# or pattern in it, and replaces all occurrences of that string with another string.

# Read content from the file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\search.txt", "r") as file:
    content = file.read()

# Search for a specific string and replace it
search_string = "old_string"
replace_string = "new_string"
new_content = content.replace(search_string, replace_string)

# Write the modified content back to the file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\new_replace.txt" , "w") as file2:
    file2.write(new_content)

print("Search and replace completed successfully!")
