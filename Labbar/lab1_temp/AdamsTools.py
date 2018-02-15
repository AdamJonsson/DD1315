def longNameGenerator(nameToRepeat, iterations, newline = False):
    theLongName = ""
    for i in range(0, iterations):
        theLongName += nameToRepeat
        if newline: 
            theLongName += "\n"
    return theLongName

def requiredInput(inputText, errorText):
    while True:
        userInput = input(inputText)
        if userInput != "": 
            break
        else: 
            print(errorText, "\n")
    return userInput