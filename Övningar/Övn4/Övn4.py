import os
from terminalColor import bcolors

def creatFileFromString(filename, string):
    if(os.path.isfile(filename)):
        print("Filen exesterar redan")
        return False
    fileWriteObject = open(filename, "w")
    fileWriteObject.write(string)
    fileWriteObject.close()
    print(bcolors.OKGREEN + "File is now created" + bcolors.ENDC)
    return True

def printFileOnScreen(filename):
    if(os.path.isfile(filename) == False):
        print("Filen exesterar inte")
        return False
    fileReadObject = open(filename, "r")
    print(fileReadObject.read())

print("\n\n###########")
creatFileFromString("FileTest.txt", "Hejsan")
printFileOnScreen("FileTest.txt")
print("########### \n\n")