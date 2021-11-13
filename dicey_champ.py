import random

# functions we need to build
# 1- create players
# 2- setup game
# 3- roll dice
# 4- next round
# 5- results
# 6- play again

players = {}


def create_player():
    players_name = input("Player's name: ")
    players[players_name] = 0
    add_more_players = input("Add new player? [yes/no] ")
    if add_more_players == "yes":
        create_player()
    else:
        setup_game()


def setup_game():
    number_of_rounds = int(input("How many rounds do you want to play? "))
    max_dice_number = int(input("How many dice sides do you want to play with? "))
    if (number_of_rounds <= 0) or (max_dice_number <= 1):
        print("You need to pick a number bigger than 1")
        new_nor = int(input("How many rounds do you want to play? "))
        new_mdn = int(input("How many dice sides do you want to play with? "))
        roll_dice(new_nor, new_mdn)

    roll_dice(number_of_rounds, max_dice_number)


def roll_dice(number_of_rounds, max_dice_number):
    for each_round in range(0, number_of_rounds):
        for player in players:
            dice_value = random.randint(1, max_dice_number)
            print(f"{player} got: {dice_value}")
            # players[player] = players[player] + dice_value
            players[player] += dice_value
    
    results()


def results():
    for player in players:
        score = players[player]
        print(f'{player} got a total of {score}')

    play_again()


def play_again():
    answer = input("Do you want to play again? [yes/no]")
    if answer == "yes":
        reuse_players = input("Do you want to use the same players? [yes/no] ")
        if reuse_players == "yes":
            setup_game()
        if reuse_players == "no":
            create_player()
        else:
            play_again()
    if answer == "no":
        print("Cool! It was a good game!")
    else:
        play_again()


create_player()