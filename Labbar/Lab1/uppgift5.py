import sys, math

def myFunction:
    mathValue = math.pi**2/6
    sumValue = 0

    n = int(input("\nn: "))
    for i in range(1, n + 1):
        sumValue += 1/(i**2)

    print("Math value: ", mathValue)
    print("Sum value: ", sumValue)
    print("The diffrens between the values", (mathValue - sumValue), "\n")

    userInput = input("Run again? y/n")
    if(userInput == "y") myFunction()
    else return true
