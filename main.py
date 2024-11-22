import os
from parse import parse
from countWords import countWords
from createStrings import createWordsStrings



def main():

    userInput = os.path.expanduser('~/workspace/github.com/Thom590/bookbot/books/frankenstein.txt')

    myParse = parse(userInput) 
    print(myParse)

    wordsStrings = createWordsStrings(myParse)
    totalWords = countWords(wordsStrings)
    print(totalWords)
    

    
main()