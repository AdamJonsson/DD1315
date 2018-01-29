
import copy
import math
import random

# uppgift 0 (Trololo)
def getLine(lenght = 30, char = "-"): 
    """ Retunerar en bokstav ett antal gånger """
    lineString = ""
    for i in range(0, lenght):
        lineString += char
    return lineString

# Uppgift 1 (givet)

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
print(getLine(50, "#"), "\n")
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)
def my_function(x):
    """ x (Int eller float). Retunerar något konstigt mattetal? """
    tempValue = math.sin(x)**2 + x**2
    return tempValue

# Uppgift 3 (att skrivas)
def roll_dice(n):
    """
        Returnerar två saker: 
        En lista med alla slag 
        En summa av alla slag
    """
    diceList = []
    for i in range(n):
        diceList.append(random.randint(1, 6))
    return (diceList, sum(diceList))

# Uppgift 4 (att skrivas)
def my_sort_list(listToSort):
    """
        Sorterar en lista, minst till störst. 
        Retunerar inget värde, listan genom argumentet referaras 
    """
    for i in range(len(listToSort)):
        for a in range(1, len(listToSort) - i):
            if(listToSort[a - 1] > listToSort[a]):
                tempVar = listToSort[a]
                listToSort[a] = listToSort[a-1]
                listToSort[a-1] = tempVar


# Uppgift 5 (att skrivas)
def bandit_language(wordToTranslate):
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z", "W", "Y"]
    newWord = ""
    for char in wordToTranslate:
        newWord += char
        if(char.upper() in consonants):
            newWord += "o"
    return newWord

# Uppgift 6
def make_bandit_dictionary(theDictionary):
    """ 
        OBS: Följande struktur av listan måste följas.
        {
            foo_1: [string_1, string_2, ...]
            foo_2: [string_1, string_2, ...],
            foo_3: [string_1, string_2, ...],
            ...
        }
    """
    newDictionary = {}
    for keyWord in theDictionary: 
        newList = []
        for listElement in theDictionary[keyWord]:
            newList.append(bandit_language(listElement))
        newDictionary[keyWord] = newList
    return newDictionary

