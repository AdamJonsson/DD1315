import sys

print(1 == 0.99)
print(1 == 0.99999999999)
print(1 == 0.99999999999999999999) #Genom att en float kan max ha 15 decimaler så avrundas värdet 0.99999999999999999999 till 1.

print("Float max digits: ", sys.float_info.dig)



