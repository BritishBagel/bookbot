def BookBotReportPrintText(bookFileName, wordCount, charactersCount):
    PrintString = "============ BOOKBOT ============"
    PrintString += f"\nAnalysing book found at {bookFileName}..."
    PrintString += "\n----------- Word Count ----------"
    PrintString += f"\nFound {wordCount} total words"
    PrintString += "\n--------- Character Count -------"
    for Character in charactersCount:
        PrintString += f"\n{Character["Character"]}: {Character["Occurrences"]}"
    PrintString += "\n============= END ==============="
    return PrintString