age = int(input("How old are you?\n"))

#the double // means it will return just the whole number and the modulus (%) returns only the remainder
decades = age//10
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old.")