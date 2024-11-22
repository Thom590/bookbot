import os
from parse import parse
from countWords import countWords
#from createStrings import createStrings


def main():

    userInput = os.path.expanduser(input("Define path to file:"))

    myParse = parse(userInput) 
    print(myParse)

    totalWords = (countWords(myParse))
    print(totalWords)
    #print(file_content)
    #print(i)
    
main()