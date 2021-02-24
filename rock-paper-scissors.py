import random
import math
import time
import sys


def play_game():
    print("Rock!  ", end="", flush=True)
    time.sleep(1)
    print("Paper!  ", end="", flush=True)
    time.sleep(1)
    print("Scissors!  ", end="", flush=True)
    time.sleep(1)
    print("SHOOT!\n\n")
    label = ["rock", "paper", "scissors"]
    robot_choice = label[random.randint(0, 2)]

    user_choice = input("rock? paper? scissors? ")
    print_result = "Game picked " + robot_choice+"\n"
    result = 0
    if robot_choice == "rock":
        if user_choice == "rock":
            print_result += "DRAW!! Rock and Rock."
            result = 1
        elif user_choice == "paper":
            print_result += "You win! Paper beats Rock!!"
            result = 2
        elif user_choice == "scissors":
            print_result += "You lose. Rock beats Scissors."
    elif robot_choice == "paper":
        if user_choice == "rock":
            print_result += "You lose. Paper beats Paper."
        elif user_choice == "paper":
            print_result += "DRAW!! Paper and Paper."
            result = 1
        elif user_choice == "scissors":
            print_result += "You win! Scissors beats Paper!!"
            result = 2
    elif robot_choice == "scissors":
        if user_choice == "rock":
            print_result += "You win! Rock beats Scissors!!"
            result = 2
        elif user_choice == "paper":
            print_result += "You lose. Scissors beats paper."
        elif user_choice == "scissors":
            print_result += "DRAW!! Scissors and scissors."
            result = 1

    print("\n\n"+print_result)
    robot_choice = None
    return result


win, lose, draw = 0, 0, 0
rounds = 3
round_label = 1

for round in range(rounds):
    print("\n\nROUND " + str(round_label) + "\nLET'S GO!!!\n\n")
    current_round = play_game()
    if current_round == 0:
        lose += 1
    elif current_round == 1:
        draw += 1
    elif current_round == 2:
        win += 1
    round_label += 1

print("\n\n**********\n\nResults:\n\nWins: "+str(win)+"\nLoss: " +
      str(lose)+"\nDraws: "+str(draw)+"\n\n")

if win > lose:
    print("YOU ARE THE WINNER!!")
elif win == lose:
    print("IT'S A DRAW!!")
else:
    print("You are THE LOSER!!!")
print("\n\n**********\n\n")
