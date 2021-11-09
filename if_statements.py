import random
# Data types: Strings and Integers
# transform int into a str 
# transform str into an int

# methods: 
# input()
# print()

#Version 1
# number = 5
# guess = input("guess the number: ")

# if int(guess) < number:
#     print("Your guess is too low.")
# if int(guess) > number:
#     print("your guess is too high.")
# if int(guess) == number:
#     print("Well done!")

#--------------------
#Version 2
# number = random.randint(1, 10)
# guess = input("guess the number: ") 

# if int(guess) < number: 
#     print("Your guess is too low.")
# if int(guess) > number: 
#     print("your guess is too high.")
# if int(guess) == number: 
#     print("Well done!")

# print(f"The number was: {number}")

#----------------------
#Version 3
number = random.randint(1, 10)
guess = int(input("guess the number: "))

if guess < number: 
    print("Your guess is too low.")
if guess > number: 
    print("your guess is too high.")
if guess == number: 
    print("Well done!")

print(f"The number was: {number}")