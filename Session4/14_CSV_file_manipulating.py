# 3. CSV File Manipulation:
#    Write a Python program that reads data from a CSV file, performs some operations
# (e.g., calculating the total, average, or maximum value of a column), and
# then writes the results to a new CSV file.

import csv

# Read data from the input CSV file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\cr_all.txt", "r", newline='') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Perform operations on the data (e.g., calculate total of a column)
total_row = len(data)
total_column = len(data[0])

# Write the results to a new CSV file
with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\cr_all_output.txt", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Total number of Row in CSV file is "])
    writer.writerow([total_row])
    writer.writerow(["Total number of Column in CSV file is "])
    writer.writerow([total_column])

print("Results written into output.csv")


with open(r"C:\Users\Hp\OneDrive\Desktop\DATA\Downloads\cr_all_output.txt" , "r") as read_file :
    print(read_file.read())

