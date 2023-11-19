# Rock Paper Scissors game

# Importing random module
import random as r

# Welcoming user
print('''
      Welcome to rock paper scissors game!\n Hope you enjoy playing this game!
      ''')
name = input("Enter your name : ")
print(F"Hi, {name}")


# Main function for game!


def main(name):
    # All choices in game
    choices = ["rock", "paper", "scissors"]

# Computer random coice
    Cchoice = r.choice(choices)

# Taking input the user choice
    Hchoice = None
    while Hchoice not in choices:
        Hchoice = input("Rock , Paper or scissors (pickone) -->").lower()

# Winner deciding blocks
    if Hchoice == Cchoice:
        flag = None

    elif Hchoice == 'scissors':
        if Cchoice == 'paper':
            flag = True
        else:
            flag = False

    elif Hchoice == 'paper':
        if Cchoice == 'rock':
            flag = True
        else:
            flag = False

    elif Hchoice == 'rock':
        if Cchoice == 'scissors':
            flag = True
        else:
            flag = False

# Printing who won and who lose
    if flag == None:
        result = "Tie"
    elif flag == True:
        result = "You win!"
    elif flag == False:
        result = "You lose!"
    print(
        f" Computer chooses : {Cchoice}\n {name} chooses : {Hchoice}\n {result}")

    x = input("Do you want to play again (Y/N) ?\n")
    if x.upper() == 'Y':
        main(name)
    else:
        # Thanking player for playing
        print("Thank you for playing :)")


# Running the game
main(name)
