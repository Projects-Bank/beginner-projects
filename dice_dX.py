import random

5
#Roll dice function
def roll_dice(number_of_sides):
    dice_value = random.randint(1, number_of_sides)
    print(f"You got a {dice_value}!")

    create_dice()


def create_dice():
    number_of_sides = int(input("how many sides your dice has? "))
    if (number_of_sides <= 1) or (number_of_sides > 5000):
        print("The number of sides has to be between 1 and 5000")
        create_dice()
    else:
        roll_dice(number_of_sides)


create_dice()