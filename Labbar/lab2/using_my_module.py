
import my_module

# Uppgift 1 (givet)
y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)
print(my_module.getLine(50))
print("my_function retunerar: ", my_module.my_function(10))
print(my_module.getLine(50))

# Uppgift 3 (att skrivas)
diceSum = my_module.roll_dice(10)
print("Summan av slagen", diceSum)
print(my_module.getLine(50))

# Uppgift 4 (att skrivas)
listToSort = [1, 6, 3, 7,8, 3, 2, 7, 4, 8, 1, 8, 4, 1, 9, 4, 2]
my_module.my_sort_list(listToSort)
print("Sorterad lista: ", listToSort)
print(my_module.getLine(50))

# Uppgift 5 (att skrivas)
print("Konstig mening: ", my_module.bandit_language("This is a test to see if everthing is working"));

# Uppgift 6 (givet)
animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }


# Uppgift 6 (att skrivas)
newAnimals = my_module.make_bandit_dictionary(animals)
print("Nya djuren: ", newAnimals)
print(my_module.getLine(50,))

# Överigt
print()
print(my_module.getLine(50, "#"))