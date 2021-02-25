import random
import math
import time
import sys


def get_random_robot_choice():
    label = ["rock", "paper", "scissors"]
    return label[random.randint(0, 2)]


def decide_winner(payer_one, robot_choice):
    result = 0
    print_result = ""
    print("\nYou chose "+payer_one + " and Robot chose "+robot_choice)
    if robot_choice == "rock":
        if payer_one == "rock":
            print_result += "DRAW!! Rock and Rock."
            result = 1
        elif payer_one == "paper":
            print_result += "You win! Paper beats Rock!!"
            result = 2
        elif payer_one == "scissors":
            print_result += "You lose. Rock beats Scissors."
    elif robot_choice == "paper":
        if payer_one == "rock":
            print_result += "You lose. Paper beats Paper."
        elif payer_one == "paper":
            print_result += "DRAW!! Paper and Paper."
            result = 1
        elif payer_one == "scissors":
            print_result += "You win! Scissors beats Paper!!"
            result = 2
    elif robot_choice == "scissors":
        if payer_one == "rock":
            print_result += "You win! Rock beats Scissors!!"
            result = 2
        elif payer_one == "paper":
            print_result += "You lose. Scissors beats paper."
        elif payer_one == "scissors":
            print_result += "DRAW!! Scissors and scissors."
            result = 1
    print(print_result)
    return result


class game:
    def __init__(self, rounds, player_name):
        self.rounds = rounds
        self.player_name = player_name
        self.player_score = 0
        self.robot_score = 0

    def play_game(self):

        # for round in range(self.rounds):
        current_round = 1
        while True:
            print("\n\n**********\n\n")
            print("ROUND " + str(current_round) + " start!!")
            print("Rock!  ", end="", flush=True)
            time.sleep(1)
            print("Paper!  ", end="", flush=True)
            time.sleep(1)
            print("Scissors!  ", end="", flush=True)
            time.sleep(1)
            print("SHOOT!\n")
            user_choice = input("Choose rock, paper or scissors? ")
            robot_choice = get_random_robot_choice()
            round_result = decide_winner(user_choice, robot_choice)
            if round_result == 0:  # lose
                self.robot_score += 1
            elif round_result == 1:  # draw
                if self.robot_score == self.player_score:
                    self.rounds += 1
            elif round_result == 2:  # win
                self.player_score += 1

            if self.rounds == current_round:
                break

            print("\n"+self.player_name + " score: " +
                  str(self.player_score))
            print("ROBOT score: " + str(self.robot_score) + "\n")

            current_round += 1

    def print_results(self):
        winner = "ROBOT"
        results = "\n\n**********\n\n"
        if self.player_score > self.robot_score:
            winner = self.player_name
            results += "YES! You are the WINNER!\n\n"
        else:
            results += "SORRY! You are such a loser!\n\n"
        results += "The winner is " + winner + "!!\n"
        results += self.player_name + " score: " + \
            str(self.player_score) + "\n"
        results += "ROBOT score: " + str(self.robot_score) + "\n"
        results += "\n\n**********\n\n"
        print(results)


new_game = game(3, "Gani")
new_game.play_game()
new_game.print_results()
