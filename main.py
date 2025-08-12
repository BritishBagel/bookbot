import sys

from stats import GetSortedListOfCharacters
from stats import GetNumberOfWordsInBook

from print import BookBotReportPrintText

def Main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    BookFilePath = sys.argv[1] #"books/frankenstein.txt"
    WordCount = GetNumberOfWordsInBook(BookFilePath)
    CharacterCountDict = GetSortedListOfCharacters(BookFilePath)
    print(BookBotReportPrintText(BookFilePath, WordCount, CharacterCountDict))

Main()