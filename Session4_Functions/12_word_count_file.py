with open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice.txt" , "r") as file :
    content = file.read()
    print("The file of data : " , content)


    # Find the count of Words in file

    word_count = len(content.split())

    print("Count word of this file is :" , word_count)

    # Find total count of words in file

    words_count = len(content)

    print("Total Count words of this file is :", words_count)

    # Find how many lines in file

    line_count = content.count("\n") + 1


    print(line_count)

