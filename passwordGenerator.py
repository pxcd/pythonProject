#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#letter generator
myLetters = ""
for x in range(0, nr_letters):
  myLetters += random.choice(letters)
# print(myLetters)
####

#symbol Generator
mySymbols = ""
for y in range(0, nr_symbols):
  mySymbols += random.choice(symbols)


#number Generator
myNumbers =""
for z in range(0, nr_numbers):
  myNumbers += random.choice(numbers)
# print(myNumbers)



myPassword = (myLetters + myNumbers + mySymbols)
print(f"my password is {myPassword}")

l = list(myPassword)
print(l)


random.shuffle(l)



full_str = ''.join([str(elem) for elem in l])

print (full_str)



# print(k)