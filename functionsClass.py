import os
import random


class FunctionsClass:
    global color_red, color_green, color_end
    color_red= '\033[31m'
    color_green = '\033[32m'
    color_end = '\033[0m'

    @staticmethod
    def get_board(numbers):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{numbers[0]}{"|"}{numbers[1]}{"|"}{numbers[2]}')
        print("_|_|_")
        print(f'{numbers[3]}{"|"}{numbers[4]}{"|"}{numbers[5]}')
        print("_|_|_")
        print(f'{numbers[6]}{"|"}{numbers[7]}{"|"}{numbers[8]}')
        print(" | |")
        print("\n")

    @staticmethod
    def update_tic_tac_toe(player_number, number_list, player_symbol):
        for item in range(len(number_list)):
            if number_list[item] == player_number:
                number_list[item] = player_symbol
        return number_list

    @staticmethod
    def validate_if_won_or_drawn(number_list):
        actual_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        winning_combinations = {"1": [1, 2, 3], "2": [4, 5, 6], "3": [7, 8, 9], "4": [1, 4, 7], "5": [2, 5, 8],
                                "6": [3, 6, 9], "7": [1, 5, 9], "8": [3, 5, 7]}
        for index in winning_combinations.keys():
            first = winning_combinations[index][0]
            second = winning_combinations[index][1]
            third = winning_combinations[index][2]
            if number_list[first - 1] == number_list[second - 1] == number_list[third - 1]:
                return "Won"
        if not (any(item in actual_numbers for item in number_list)):
            return "Drawn"
        else:
            return "Continue"

    @staticmethod
    def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    @staticmethod
    def replay():
        while True:
            playagain = input('Do you want to play again? Enter Yes or No: ')
            if playagain == 'yes' or playagain == 'y':
                return True
            elif playagain == 'no' or playagain == 'n':
                return False
            else:
                print(color_red+"Please choose a valid input: yes/no\n"+color_end)

    @staticmethod
    def assign_marks(turn):
        while True:
            if turn == "Player 1":
                player1 = input(f'Player 1: Do you want to choose {"X"} or {"O"}?\n')
                if player1 == "X" or "x":
                    player1 = color_red + "X" + color_end
                    player2 = color_green + "O" + color_end
                    break
                elif player1 == "O" or "o":
                    player1 = color_green + "O" + color_end
                    player2 = color_red + "X" + color_end
                    break
                else:
                    print(color_red + "Please choose a valid input." + color_end)
                    continue
            else:
                player2 = input(f'Player 2: Do you want to choose {"X"} or {"O"}?\n')
                if player2 == "X" or "x":
                    player2 = color_red + "X" + color_end
                    player1 = color_green + "O" + color_end
                    break
                elif player2 == "O" or "o":
                    player2 = color_green + "O" + color_end
                    player1 = color_red + "X" + color_end
                    break
                else:
                    print(color_red + "Please choose a valid input." + color_end)
                    continue
        return player1, player2
