import sys
import AdamsTools as ATools

userInput = ATools.requiredInput("What is your name? My name is: ", "You can not enter an empty text")
longUsername = ATools.longNameGenerator(userInput, 39, True)
print(longUsername)
