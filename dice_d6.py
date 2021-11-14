import random


def roll_dice():
    dice_value = random.randint(1, 6)
    print('Rolling the dice...')
    print(f'You got a {dice_value}')
    
    roll_again()


def roll_again():
    answer = input("Do you want to play again? [yes/no]")
    if answer == "yes":
        roll_dice()
    elif answer == "no":
        print("No dice rolling!")
    else:
        print("are u drunk?!?")


roll_dice()


    
