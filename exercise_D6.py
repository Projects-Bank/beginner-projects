import random


def roll_dice(roll="yes"):
    dice_value = random.randint(1, 10)
    print('Rolling the dice...')
    print(f'You have a {dice_value}')
    answer = input("Would you like to play again? [yes/no]")
    roll_again(answer) 


def roll_again(answer):
    if answer == "yes":
        roll_dice(answer)
    elif answer == "no":
        print("No dice rolling!")
    else:
        print("are you stupid!")


roll_dice()