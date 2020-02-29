# Session: 2 
# Date: 12/jan/2020
# Topic: String Functions

#1. upper - upper function converts lower case string into upper case.
fruit="pineapple"
print(fruit.upper())

#2. lower- It converts upper case string into lower case.
fruit="APPLE"
print(fruit.lower())

#3. swapcase - Swapcase function is used to convert lower case letter into uppercase and uppercase into lowercase.
fruit="MaNgO"
print(fruit.swapcase())

#4. count- Count function counts position of alphabet.
fruit="Cheery"
print(fruit.count("r"))

#5. Capitalize
name='chinmay'
c_name=name.capitalize()
print(c_name)

#6. Title
name="chinmay potdar"
print(name.title())

#7. center
name="chinmay"
print(name.center(30))

#8. Strip (Removing the spaces)
name="  chinmay   p  "
print(name.strip())

#9. lstrip
name="  chinmay   p  "
print(name.lstrip())


#10. rstrip
name="  chinmay   p  "
print(name.rstrip())

#11. Replace 
name="cello"
print(name.replace('c','h'))

#12. Startwith
car="Hondacity"
print(car.startswith("H"))

#13. endswith()
car="Hondacity"
print(car.endswith('y'))
