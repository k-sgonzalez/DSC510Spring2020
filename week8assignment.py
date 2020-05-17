"""
File DSC510_T303 Week 8 Programming Assignment
Name: Kim Gonzalez
Date: 17May2020
Course: DSC510_T303 Intro to Python Programming
Details:
We will create a program which performs three essential
operations. It will process this .txt file: Gettysburg.txt.
Calculate the total words, and output the number of
occurrences of each word in the file.

There will be the following functions:

add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

Process_line: There is some work to be done to process the line: strip off various characters,
split out the words, and so on. Parameters are a line and the dictionary. It calls the function
add word with each processed word. No return value.

Pretty_print: Because formatted printing can be messy and often particular to each situation
(meaning that we might need to modify it later), we separated out the printing function. The parameter
is a dictionary. No return value.

main: We will use a main function as the main program. As usual, it will open the file and call
process_line on each line. When finished, it will call pretty_print to print the dictionary.

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

def pretty_print(dictionary): #function prints everything into a "pretty" format
    spacer = ' ' * 24
    line_sep = '_' * 35
    print("The total number of words is:",len(dictionary))
    print("Word" + spacer + "Count")
    print(line_sep)
    count_list = list(dictionary.items())
    count_list.sort(key=lambda x: x[1], reverse=True)
    for word, count in count_list:
            print("{:23}    {:4}".format(word, count))

def main(): #this is where the other functions will be called on
    dictionary = dict()
    gba_file = open('Gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, dictionary)
    pretty_print(dictionary)

main()
