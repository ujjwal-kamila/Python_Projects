# main.py
# Rock Paper Scissors Game Logic

import random

def play_rps(user_choice):
    """
    Returns computer choice and result
    """
    item_list = ["Rock", "Paper", "Scissor"]
    comp_choice = random.choice(item_list)

    if user_choice == comp_choice:
        result = "Tie"
    elif user_choice == "Rock":
        result = "You Win" if comp_choice == "Scissor" else "Computer Wins"
    elif user_choice == "Paper":
        result = "You Win" if comp_choice == "Rock" else "Computer Wins"
    elif user_choice == "Scissor":
        result = "You Win" if comp_choice == "Paper" else "Computer Wins"
    else:
        result = "Invalid Choice"

    return comp_choice, result


# Terminal working code
# # Rock paper scissor game

# """
# 1- Input from user(Rock, paper, scissor)
# 2- Computer choice (Computer will choose randomly not conditionally)
# 3- Result print

# Cases:
# A- Rock
# Rock - Rock = tie
# Rock - Paper = Paper win
# Rock - scissor = Rock win

# B- Paper
# Paper - Paper = tie
# Paper - Rock = Paper win
# Paper - Scissor = Scissor win

# C- Scissor
# Scissor - Scissor = tie
# Scissor - Rock = Rock win
# Scissor - Paper = Scissor win

# """

# import random
# item_list = ["Rock", "Paper", "Scissor"]

# user_choice = input("Enter your move = Rock, Paper, Scissor= ")
# comp_choice = random.choice(item_list)

# print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

# if user_choice == comp_choice:
#     print("Both chooses same: = Match Tie")

# elif user_choice == "Rock":
#     if comp_choice == "Paper":
#         print("Paper covers Rock = Computer Win")
#     else:
#         print("Rock smashes Scissor = You win")

# elif user_choice == "Paper":
#     if comp_choice == "Scissor":
#         print("Scissor cuts paper, Computer Win")
#     else:
#         print("Paper covers rock, You win")

# elif user_choice == "Scissor":
#     if comp_choice == "Paper":
#         print("Scissor cuts paper, You win")
#     else:
#         print("Rock smashes scissor, Computer win")

