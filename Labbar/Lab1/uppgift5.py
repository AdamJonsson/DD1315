import sys, math

def myFunction():
    mathValue = math.pi**2/6
    sumValue = 0

    n = int(input("\nn: "))
    for i in range(n):
        sumValue += 1/(i**2)

    print("Math value: ", mathValue)
    print("Sum value: ", sumValue)
    print("The difference between the valåäöues", (mathValue - sumValue), "\n")

    userInput = input("Run again? y/n")
    if(userInput == "y"):
         myFunction()
    else: 
        return True

myFunction()