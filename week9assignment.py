"""
File DSC510_T303 Week 9 Programming Assignment
Name: Kim Gonzalez
Date: 18May2020
Course: DSC510_T303 Intro to Python Programming
Details:
For this week we will modify our Gettysburg processing program from week 8 in
order to generate a text file from the output rather than printing to the
screen. Your program should have a new function called process_file which
prints to the file (this method should almost be the same as the pretty_print
function from last week. Keep in mind that we have print statements in main as
well. Your program must modify the print statements from main as well.

- Create a new function called process_file. This function will perform the
same operations as pretty_print from week 8 however it will print to a file
instead of to the screen.
- Modify your main method to print the length of the dictionary to the file
as opposed to the screen.
- This will require that you open the file twice. Once in main and once in
process_file.
- Prompt the user for the filename they wish to use to generate the report.
- Use the filename specified by the user to write the file.
- This will require you to pass the file as an additional parameter to your
new process_file function.

**Include appropriate comments throughout program
"""
import string #this helps us with removing punctuation from string in process_line

def add_word (word, dictionary_word):
    if word in dictionary_word:
            dictionary_word[word] = dictionary_word[word]+1 #this begins counting multiple word instances
    else:
        dictionary_word[word] =1 #this starts word count at 1

def process_line(line, dictionary):
    line = line.lower() #converts all words to lowercase
    line = line.strip() #removes all unwanted spaces and lines
    line = line.translate(line.maketrans("", "", string.punctuation)) #removes unwanted punctuation
    words = line.split()  # splits the words from the text line by line
    for word in words:
        add_word(word, dictionary)

#def pretty_print(dictionary): #function prints everything into a "pretty" format
#    spacer = ' ' * 24
#    line_sep = '_' * 35
#    print("The total number of words is:",len(dictionary))
#    print("Word" + spacer + "Count")
#    print(line_sep)
#    count_list = list(dictionary.items())
#    count_list.sort(key=lambda x: x[1], reverse=True)
#    for word, count in count_list:
#            print("{:23}    {:4}".format(word, count))

def process_file(dictionary, new_file): #new function similar to pretty_print, except will create new file
    word_total = len(dictionary)
    spacer = ' ' * 24
    line_sep = '_' * 35
    new_line = "\n"
#    print("The total number of words is:",len(dictionary))
#    print("Word" + spacer + "Count")
#    print(line_sep)
    count_list = list(dictionary.items())
    count_list.sort(key=lambda x: x[1], reverse=True)
    new_file_output = open(new_file, 'w') #this prompts for creating new file where old pretty_print will go
    new_file_output.write("The total number of words is: {}\n".format(word_total))
    new_file_output.write("Word" + spacer + "Count" + new_line)
    new_file_output.write(line_sep + new_line)
    for word, count in count_list:
        new_file_output.write("{:23}    {:4}".format(word, count) + new_line)

def main(): #this is where the other functions will be called on
    dictionary = dict()
    gba_file = open('Gettysburg.txt', 'r')
    new_file_name = input("Please name your new file:\n") #ask user input for new file name
    if ".txt" not in new_file_name: #this will make sure a .txt file is generated
        new_file = new_file_name + ".txt"
    else:
        new_file = new_file_name
    for line in gba_file: #this calls on the process_line and the new process_file functions
        process_line(line, dictionary)
#    pretty_print(dictionary)
    process_file(dictionary, new_file)
main()
