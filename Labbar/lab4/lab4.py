from terminalColor import bcolors

class Account:

    def __init__(self, name, money, pin_code):
        self.name = name
        self.money = money
        self.pin_code = pin_code
        self.transactions = []
        print("Skapade ett nytt konto")

    def __str__(self):
        accountOwner = "Konto: " + self.name + "\n"
        accountMoney = "Pengar: " + str(self.money) + "sek \n"
        
        return (accountOwner + accountMoney + self.print_history())

    def print_history(self):
        accountTrasactions = "\tHistorik\n"
        for amountOfMoney in self.transactions: 
            accountTrasactions += "\t\tTransaktion: " + str(amountOfMoney) + "sek\n"
        return accountTrasactions

    def deposit(self, amount):
        self.money += amount
        self.transactions.append(amount)
        return bcolors.OKGREEN + "Du lyckades lägga till " + str(amount) + "sek i dit konto!" + bcolors.ENDC

    def withdrawal(self, amount, pin):
        if(self.ok_PIN(pin)):
            if(self.money > amount):
                self.transactions.append(-amount)
                return bcolors.OKGREEN + "Lyckades ta ut " + str(amount) + " ur ditt konto" + bcolors.ENDC
            else:
                return bcolors.WARNING+"Du har inte tillräckligt med pengar..."+bcolors.ENDC
        else:
            return bcolors.FAIL+"Fel PIN!"+bcolors.ENDC

    def ok_PIN(self, pin):
        if(self.pin_code == pin):
            return True
        return False

    def change_PIN(self, old_pin, new_pin):
        if(self.ok_PIN(old_pin)):
            self.pin_code = new_pin
            return bcolors.OKGREEN + "Lyckades byta PIN" + bcolors.ENDC
        else:
            return bcolors.FAIL+"Fel PIN!"+bcolors.ENDC

class PremiumAccount(Account):
    def withdrawal(self, amount, pin):
        if(self.ok_PIN(pin)):
            if(self.money > amount):
                self.transactions.append(-amount)
                return bcolors.OKGREEN + "Lyckades ta ut " + str(amount) + " ur ditt konto" + bcolors.ENDC
            else:
                return bcolors.WARNING+"Tyvärr finns inte tillräckligt med pengar. Du kanske vill ha ett lång?"+bcolors.ENDC
        else:
            return bcolors.FAIL+"Fel PIN!"+bcolors.ENDC

def find_account(accountName):
    try:
        account = account_dict[accountName]
        return account
    except KeyError:
        print(bcolors.FAIL+"Hittar inte kontot..."+bcolors.ENDC)
        return False

def read_account_from_file(file_name):
    pass

def write_accounts_to_file(accounts, file_name):
    pass

def get_int_input(prompt_string):
    while True:
        try:
            inputValue = int(prompt_string)
            break
        except ValueError:
            print(bcolors.WARNING+"Måste vara ett heltal"+bcolors.ENDC)
            prompt_string = input("Svara igen: ")
    return inputValue

def display_accounts(account_dict):
    for key, account in account_dict.items():
        print(account)

def menu_choice():
    choice = get_int_input(input("Ditt svar: "))
    return choice


def execute(choice):
    if(choice == 1):
        print("\nSkapar ett nytt konto")
        accountName = input("\tNamn på konto: ") 
        accountMoney = get_int_input(input("\tPengar att lägga till: "))
        accountPin = get_int_input(input("\tNya PIN: "))
        account_dict[accountName] = Account(accountName, accountMoney, accountPin)

    elif(choice == 2):
        print("\nLägger till pengar")
        accountName = input("\tNamn på konto: ") 
        account = find_account(accountName)
        if(account):
            amountToAdd = get_int_input(input("\tMängd pengar: "))
            message = account.deposit(amountToAdd)
            print(message)
        
    elif(choice == 3):
        print("\nTa ut pengar")
        accountName = input("\tNamn på konto: ") 
        account = find_account(accountName)
        if(account):
            amountToTake = get_int_input(input("\tMängd pengar: "))
            inputPin = get_int_input(input("\tPIN: "))
            message = account.withdrawal(amountToTake, inputPin)
            print(message)
        
    elif(choice == 4):
        print("\nÄndra PIN")
        accountName = input("\tNamn på konto: ") 
        account = find_account(accountName)
        if(account):
            oldPin = get_int_input(input("\tNuvarande PIN: "))
            newPin = get_int_input(input("\tNytt PIN: "))
            message = account.change_PIN(oldPin, newPin)
            print(message)

    elif(choice == 5):
        accountName = input("\tNamn: ") 
        account = find_account(accountName)
        if(account):
            print(account_dict[accountName].print_history())
    
    input("Tryck enter för att forsätta.\n")

def menu():
    userInput = 0
    while True:
        print("###################################")
        print("Vad vill du göra?\n", "\t1 - Skapa ett nytt konto\n", "\t2 - Lägga in pengar\n", "\t3 - Ta ut pengar\n", "\t4 - Ändra PIN\n", "\t5 - Visa historik\n", "\t6 - Avlsuta")
        userInput = menu_choice()
        if (userInput == 6 or userInput == "123"): 
            break
        execute(userInput)

account_dict = {}
account_dict["Lisa"] = Account("Lisa", 200, 1111)
account_dict["Kalle"] = Account("Kalle", 100, 2222)
account_dict["Kim"] = Account("Kim", 300, 3333)
account_dict["Douglas"] = PremiumAccount("Douglas", 1000, 1234)
def main():
    menu()

if __name__ == "__main__":
    main()