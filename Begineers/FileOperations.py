print("\n *** File Operations *** \n ")

def count_words_lines(getFile):
    num_words, num_lines = 0,0
    with open(getFile, 'r') as f:
        for line in f:
            num_lines += 1
            num_words += len(line.split())
    f.close()
    print("\n FileName : {} \t Count of Words : {} \t Count of Lines : {} ".format(getFile, num_words, num_lines))

def file_read(getFile):
    print("\n Content of file ({}) : ".format(getFile))
    print("**"*20,"\n")
    num_words, num_lines = 0,0
    with open(getFile, 'r') as f:
        for line in f:
            print(line)
    f.close()
    print("\n","**"*20,"\n")

def write_file(getFile):
    getString = input("\n Enter the String to write into the file : ")
    temp = "\n" + getString
    with open(getFile, 'a') as f:
        f.write(temp)
    f.close()

def count_occurance_word(getFile):
    search_word = input("\n Enter the keyword to search and get the occurance : ")
    occurance_word = 0
    with open(getFile, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if i.lower() == search_word:
                    occurance_word += 1
    f.close()
    print("\n Occurance of word ({}) is {} ".format(search_word, occurance_word))

def count_occurance_letter_number_spaces(getFile):
    search_letter = input("\n Enter the letter to search and get the occurance : ")
    occurance_letter, spaces = 0,0
    with open(getFile, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if letter.lower() == search_letter:
                        occurance_letter += 1
                    elif letter.isdigit():
                        print("Numbers in the file : {}".format(letter))
                    elif letter.isspace:
                        spaces += 1
    f.close()
    print("\n Occurance of letter ({}) is {} ".format(search_letter, occurance_letter))
    print("\n Occurance of Spaces is {} ".format(spaces))

def copy_file(getFile):
    file_name = input("\n Enter the new file name : ")
    file_format = input("\n Enter the file format : ")
    file = file_name + "." + file_format
    with open(getFile) as f:
        with open(file, "w") as f1:
            for line in f:
                f1.write(line)
    file_read(file)

if __name__ == '__main__':
    file_name = input(" Enter the File Name : ")
    file_format = input(" Enter the File Format : ")
    file = file_name +"." + file_format
    while True:
        print("\n File Operations \n 1. Read File \t 2. Write File \t 3. Count Searched Keyword \n 4. Copy Content from one file to another file \
                \t 5. Display Count of searched letters and List numbers \t 6. Exit ")
        choice = int(input("\n Enter your choice : "))
        if choice == 1:
            file_read(file)
            count_words_lines(file)
        elif choice == 2:
            write_file(file)
            file_read(file)
            count_words_lines(file)
        elif choice == 3:
            file_read(file)
            count_words_lines(file)
            count_occurance_word(file)
        elif choice == 4:
            copy_file(file)
        elif choice == 5:
            file_read(file)
            count_occurance_letter_number_spaces(file)
        elif choice == 6:
            print("\n Exiting..")
            exit(0)
        else:
            print('\n Invalid Choice, Please try again..')
