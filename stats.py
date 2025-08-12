# stats.py - A file that contains functions for analysing the text

def GetBookText(bookFilePath):
    with open(bookFilePath) as f:
        return f.read()    

def GetNumberOfWordsInBook(bookFilePath):
    BookText = GetBookText(bookFilePath)
    WordCount = len(BookText.split())
    return WordCount

def GetCharacterCountDict(bookFilePath):
    BookText = GetBookText(bookFilePath)
    CharacterDict = {}
    for Character in BookText:
        LowerCharacter = Character.lower()
        if LowerCharacter in CharacterDict:
            CharacterDict[LowerCharacter] += 1
        else:
            CharacterDict.update({f"{LowerCharacter}": 1})
    return CharacterDict

def GetSortedListOfCharacters(bookFilePath):
    CharacterCountDict = GetCharacterCountDict(bookFilePath)
    SortedCharacters = []
    for Character in CharacterCountDict:
        SortedCharacters.append({"Character": Character, "Occurrences": CharacterCountDict[Character]})
    SortedCharacters.sort(reverse=True, key=SortOn)
    return SortedCharacters

def SortOn(items):
    return items["Occurrences"]