import sys
import AdamsTools as ATools

while True:
    userInput = ATools.requiredInput("Your name: ", "That is not a name human!")
    if userInput == "Kalle":
        print("Hello Kalle")
    elif userInput == "Sauron":
        print("Bye!")
        break