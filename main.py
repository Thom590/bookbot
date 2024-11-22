import os
from parse import parse
from countWords import countWords
from createStrings import createWordsList, createCharsString
from countChars import countChars

def main():

    userInput = os.path.expanduser('~/workspace/github.com/Thom590/bookbot/books/frankenstein.txt')
    myParse = parse(userInput) 

    wordsList = createWordsList(myParse)
    charsString = createCharsString(myParse)

    totalWords = countWords(wordsList)
    totalChars = countChars(charsString)

    #print(myParse)
    #print(totalWords)
    #print(totalChars)

    print('----- Begin report of books/frankenstein.txt -----')
    print(totalWords, "words found in the document")

    for key, value in totalChars.items():
        keyV = key
        valV = value
        print('The', keyV, 'charachter was found', valV, 'times')

    
main()