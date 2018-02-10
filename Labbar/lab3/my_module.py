
from shutil import copy2
from terminalColor import bcolors

import text_encryption_function as encrypt_module
import os
import random
import json

# Uppgift 1
def copyTextFile(in_file, out_file):
    """Kopierar en fil och dess innehåll. OBS: ingen felhantering."""

    copy2(in_file, out_file)

# Uppgift 2
def encryptFile(in_file, out_file):
    # Creating the encryption
    fileobject_r = open(in_file, "r")
    file_content = fileobject_r.read()
    content_encrypted = encrypt_module.encrypt(file_content)

    # Saving the encryption to a file
    fileobject_w = open(out_file, "w")
    fileobject_w.write(content_encrypted)

# Uppgift 3
def userDialogue():
    fileToSave = input("Namn på nya krypterande filen?\nFilenamn: ")

    while True:
        try:
            fileToEncrypt = input("\nVilken fil vill du kryptera?\nFilenamn: ")
            if(fileToEncrypt == "exit"): 
                break
            encryptFile(fileToEncrypt, fileToSave)
            break
        except FileNotFoundError:
            print(bcolors.WARNING+"Filen: '"+fileToEncrypt+"' finns inte. Ange en annan fil! Avsluta: exit. " + bcolors.ENDC)

    print(bcolors.OKGREEN + "Den krypterade filen '"+fileToSave+"' skapdes!" + bcolors.ENDC)

# Uppgift 4
def getIntInput(inputString):
    while True:
        try:
            userInput = input(inputString + "\n" + "Svar: ")
            userInputInt = int(userInput)
            return userInputInt
        except ValueError:
            print(bcolors.WARNING+ "Bara heltal är tillåtna!\n" + bcolors.ENDC)

# Uppgift 5, 6, 7
def printLine(char, numberOfChars):
    charString = ""
    for i in range(numberOfChars):
        stringColor = ""
        if(i % 2 == 0):
            stringColor = bcolors.WARNING
        if(i % 3 == 0):
            stringColor = bcolors.OKBLUE
        if(i % 4 == 0):
            stringColor = bcolors.OKGREEN
        if(i % 5 == 0):
            stringColor = bcolors.FAIL

        charString += (stringColor + char + bcolors.ENDC)
    return charString

def getQuizContentList(fileName):
    fileReadObject = open(fileName, "r")
    contentList = []
    while True:
        lineContent = fileReadObject.readline()
        if(lineContent == ""):
            break
        tempList = lineContent.split(";")
        contentList.append(tempList)
    return contentList

def getQuizContentListError(fileName):
    """Retunerar 0: Hittar inte filen, Retunerar 1: Inte rätt format"""

    # File error
    if(os.path.isfile(fileName) == False):
        return 0

    fileReadObject = open(fileName, "r")
    contentList = []

    while True:
        lineContent = fileReadObject.readline()
        if(lineContent == ""):
            break
        tempList = lineContent.split(";")

        # Format error
        if(len(tempList) != 4):
            return 1
        contentList.append(tempList)
    return contentList

def startQuiz():
    #quizList = getQuizContentList("Files/quiz.csv")

    while True:
        filePath = input("Vilken fil inhåller datan för quizet? ('exit' för att avsluta)\nFilnamn: ")
        quizList = getQuizContentListError(filePath)
        if(filePath == "exit"):
            return 0
        elif(quizList == 0):
            print(bcolors.WARNING + "Filen finns inte!\n" + bcolors.ENDC)
        elif(quizList == 1):
            print(bcolors.WARNING + "Filen har ej rätt format!\n" + bcolors.ENDC)
        else:
            break

    print(printLine("-", 50) + "\n" + "Hej och välkommen till den osynliga räkmackan." + "\n" + printLine("-", 50))
    for question in quizList:

        rightAnswere = question[1]
        print(bcolors.BOLD + question[0] + bcolors.ENDC)

        question.pop(0)
        random.shuffle(question)
        print("1:" + question[0].rstrip() + " 2:" + question[1].rstrip() + " 3:" + question[2].rstrip())
        userAnswere = getIntInput("Svara med (1, 2, 3)")
        
        if(userAnswere < 4 and question[userAnswere - 1] == rightAnswere):
            print(bcolors.OKGREEN + "Rätt svar!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Fel svar. Rätt är: '" +rightAnswere+ "'" + bcolors.ENDC)

        print(printLine("-", 50))
    
# Uppgift 8
def jsonTest():
    ql = getQuizContentListError("Files/quiz.csv")
    json_string = json.dumps(ql, indent=2)
    fo = open("quiz.json", "w")
    fo.write(json_string)
    fo.close()

if __name__ == '__main__':
    print(bcolors.OKBLUE+"\n#######-Start-########"+bcolors.ENDC)

    #Uppgift 1
    #copyTextFile("Files/namn.csv", "Files/my_copy.csv")

    #Uppgift 2
    #encryptFile("Files/namn.csv", "Files/secret_names.csv")

    #Uppgift 3
    #userDialogue()

    #Uppgift 4
    #getIntInput("Hur många år är du?")

    #Uppgift 5, 6, 7
    #startQuiz()

    #Uppgift 8
    jsonTest()

    print(bcolors.OKBLUE+"#######-Slut-#######\n"+bcolors.ENDC)
