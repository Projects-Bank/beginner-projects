number = 5 
guess = input("guess the number: ") 
if int(guess) < number: 
    print("Your guess is too low.") 
if int(guess) > number: 
    print("Your guess is too high") 
if int(guess) == number: 
    print("Well done!") 


