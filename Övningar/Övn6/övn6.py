class Student:

    def __init__(self, firstname, lastname):
        self.fistname = firstname
        self.lastname = lastname
    
    def getName(self):
        fullname = self.fistname + " " + self.lastname
        return fullname

    def printName(self):
        print(self.getName())

class Mediateknikstudent(Student):

    def getGrettingString(self):
        grettingString = "He"
        return grettingString

    def printGrettingString(self):
        print(self.getGrettingString())

studentOne = Student("Adam", "Jonsson")
studentOne.printName()

studentTwo = Mediateknikstudent("Madam", "Nossnoj")
studentTwo.printName()
studentTwo.printGrettingString()