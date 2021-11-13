import random


def roll_dice(roll="yes"):
    dice_value = random.randint(1, 6)
    print('Rolling the dice...')
    print(f'You got a {dice_value}')
    answer = input("Do you want to play again? [yes/no]")
    roll_again(answer)


def roll_again(answer):
    if answer == "yes":
        roll_dice(answer)
    elif answer == "no":
        print("No dice rolling!")
    else:
        print("are u drunk?!?")


roll_dice()


    
