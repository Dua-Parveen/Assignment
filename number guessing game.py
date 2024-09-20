#Create a number guessing game:


import random

print("\"Welcome to number guessing game\"", "there is 3 levels")
print("Level 1 is start:")

n = random.randint(1, 10)
guess = int(input("Enter a number from 1 to 10: "))

while n!= guess:
  if guess < n:
      print("Your guess is too low.")
      guess = int(input("Enter a number again: "))
  elif guess > n:
      print("Your number is too high")
      guess = int(input("Enter a number again:"))
  else:
      break
print("Your guess is correct")


print("Level 2 is start:")

n = random.randint(1, 30)
guess = int(input("Enter a number from 1 to 30: "))

while n!= guess:
  if guess < n:
      print("Your guess is too low.")
      guess = int(input("Enter a number again: "))
  elif guess > n:
      print("Your number is too high")
      guess = int(input("Enter a number again:"))
  else:
      break
print("Your guess is correct")


print("Level 3 is start:")

n = random.randint(1, 50)
guess = int(input("Enter a number from 1 to 50: "))

while n!= guess:
  if guess < n:
      print("Your guess is too low.")
      guess = int(input("Enter a number again: "))
  elif guess > n:
      print("Your number is too high")
      guess = int(input("Enter a number again:"))
  else:
      break
print("Your guess is correct")

print("Congratulation you complete all 3 levels")




