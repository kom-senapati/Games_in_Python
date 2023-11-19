'''
Tic-Tac-Toe game with basics of python.
'''


#Importing random module for computer choice.
import random as r


#Welcoming user.
name = input("Enter your name : ")
print(f"Hey,{name} welcome to tictactoe game!")


#Initialisation stuff.
choices = list(range(1,10)) #All the choices 1-9.
Conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)] #Conditions for winning.
d = dict(zip(choices,"_"*9)) #Backend board for the game.

#Choosing whos X and O.
user_c = ''
while user_c not in ['X', 'O']:
    user_c = input("Choose X or O : ")
if user_c == 'X':
    comp_c = 'O'
elif user_c == 'O':
    comp_c = 'X'


#Printing board (Frontend board)
print(
    f'''        ___________
       | 1 | 2 | 3 |
       |___________|
       | 4 | 5 | 6 |
       |___________|
       | 7 | 8 | 9 |
        -----------
''')


#Real mechanism
user_choice = 0
while choices:
    user_choice = input("Enter your choice : ") #Taking user's input
    if user_choice.isnumeric(): #First checking of  user's input
        user_choice = int(user_choice)
        if user_choice in choices: #Second checking of user's input
            
            
            #Updating the board
            d[user_choice] = user_c
            choices.remove(user_choice)
            comp_choice = r.choice(choices)
            d[comp_choice] = comp_c
            choices.remove(comp_choice)
            
            
            #Showing the updated board
            print(
                f'''                    ___________
                   | {d[1]} | {d[2]} | {d[3]} |
                   |___________|
                   | {d[4]} | {d[5]} | {d[6]} |
                   |___________|
                   | {d[7]} | {d[8]} | {d[9]} |
                    -----------
            ''')
            
            #Checking who wins if any winner.
            flag = None #Its for breaking the master while loop.
            for i in Conditions:
                if d[i[0]] == d[i[1]] == d[i[2]]: #Winner is found
                    if d[i[0]] == comp_c: #Computer is winner
                        print("Computer wins!")
                        flag = True
                        break #Breaking the child for loop
                    elif d[i[0]] == user_c: #User is winner
                        print(f"{name} wins!")
                        flag = True
                        break #Breaking the child for loop
            if flag == True:
                break #The loop breaks as winner is found and declared.
            
            #Handling the wrong inputs of user.
        else:
            print("Enter an appropriate choice between 1-9 which is available.")
    else:
        print("Enter an appropriate choice between 1-9.")


#Thanking the player for playing this game.
print(f"{name}, Thank You for playing in this game.")
