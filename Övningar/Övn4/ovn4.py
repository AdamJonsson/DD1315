import os

def creatFileFromString(filename, string):
    if(os.path.isfile(filename)):
        print("Filen exesterar redan")
        return False
    fileWriteObject = open(filename, "w")
    fileWriteObject.write(string)
    fileWriteObject.close()
    return True

def printFileOnScreen(filename):
    if(os.path.isfile(filename) == False):
        print("Filen exesterar inte äöå")
        return False
    fileReadObject = open(filename, "r")
    print(fileReadObject.read())

creatFileFromString("FileTest.txt", "Hejsan åäö")
printFileOnScreen("FileTest.txt")
