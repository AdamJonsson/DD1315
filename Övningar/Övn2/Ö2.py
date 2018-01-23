import sys, math


def getLine(lenght = 30, char = "-"): 
    lineString = ""
    for i in range(0, lenght):
        lineString += char
    return lineString

def rectangleArea(height, width):
    """Calculating the area of the rectangle and returning the value"""
    return height * width

def rectangleCircumference(height, width):
    """Calculating the circumference of the rectangle and returning the value"""
    return 2*height + 2*width

def thirdCharacterOfString(string): 
    """Returning the thrid character of a string"""
    tempThirdCharacter = string[2:3]
    if(tempThirdCharacter == ""):
        return False
    else:
        return tempThirdCharacter

print(getLine())
print("The area: ", rectangleArea(10, 10))
print("The circumfrence: ", rectangleCircumference(10, 10))
print("Third character: ", thirdCharacterOfString("1234"), end='\n')
print(getLine())