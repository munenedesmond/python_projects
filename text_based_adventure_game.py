"""
Context Remember Adventure? Well, we’re going to build a more basic version of that.
Task A complete text game, the program will let users move through rooms based on user 
input and get descriptions of each room. To create this, you’ll need to establish the 
directions in which the user can move, a way to track how far the user has moved 
(and therefore which room he/she is in), and to print out a description. You’ll also 
need to set limits for how far the user can move. In other words, create “walls” around 
the rooms that tell the user, “You can’t move further in this direction.”

"""

#Code 

# play_again
def play_again():
    print("Do you want to play again ?\n\tYes or No ?")
    # take input from the player
    answer = input("> ")

    if answer == "yes":
        start()
    else:
        exit()


# game over
def game_over(reason):
    print(reason)
    print("Game over")
    play_again()


# honey room
def honey_room():
    # room description
    print(
        "You are in a bright room filled with Honey and there is an exit door\n\tWhat will you do (1 or 2)\n(1)Take "
        "the honey and go through the door \n(2)Just go through the door")
    # take input from the player
    answer = input(">")

    if answer == "1":
        game_over("Nothing is free in this World, the honey was poisoned")

    elif answer == "2":
        print("Big up you are an honest man cause you minded your own business\n\tCongratulation you are the winner")
    else:
        game_over("Learn how to enter number")


# room one
def room_two():
    # room description
    print(
        'You are in dark room two.It is a great initiative you have taken toward reaching the Honey Room.\n\tThere are '
        'two '
        'doors,one to right and to the left\nWhich direction will you take? left or right??')
    # take input from the player
    answer = input(">").lower()

    if answer == "left":
        honey_room()
    elif answer == "right":
        game_over("Too bad you have hit a Wall and you are unconscious")

    else:
        game_over("You can only move on the right of left, too bad you are Stuck")


# room one
def room_one():
    # room description
    print('You have entered a dark room one.It is a great initiative you have taken towards reaching the Honey '
          'Room.\n\tThere '
          'are two doors,one to  right and to the left\nWhich direction will you take? left or right??')

    # take input from the player
    answer = input(">").lower()

    if answer == "left":
        game_over("Too bad you have hit a Wall and you are unconscious")
    elif answer == "right":
        honey_room()
    else:
        game_over("You can only move on the right of left, too bad you are Stuck")


# start
def start():
    # room description
    print('You have entered a dark mansion.It has a couple of rooms and one with full of Honey\n\tThere are two door, '
          'one to  right and to the left\nWhich direction will you take? left or right?')
    # take input from the player
    x = input(">").lower()

    if x == "left":
        room_one()

    elif x == "right":
        room_two()
    else:
        game_over("You can only move on the right of left, too bad you are Stuck")


start()
