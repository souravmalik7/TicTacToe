from functionsClass import *


class MainClass:
    def play_tic_tac_toe():
        color_red = '\033[31m'
        color_end = '\033[0m'
        color_purple = '\033[35m'
        print('Welcome to Tic Tac Toe!')
        while True:
            playgame = input("Do you want to play tic tac toe? yes/no\n")
            if playgame == 'yes' or playgame == 'y':
                number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                turn = FunctionsClass.choose_first()
                print(turn + ' will go first.')
                player1, player2 = FunctionsClass.assign_marks(turn)
            elif playgame == 'no'or playgame == 'n':
                print(color_purple+"Have a Good Day.We hope to see you soon."+color_end)
                break
            else:
                print(color_red + "Please choose a valid input.\n" + color_end)
                continue
            while True:
                FunctionsClass.get_board(number_list)
                print(f'Player1: {player1}')
                print(f'Player2: {player2}')
                if turn == 'Player 1':
                    player1_input = False
                    while not player1_input:
                        player1_number = input("Player1: Enter number 1 to 9: \n")
                        if player1_number not in number_list:
                            print(color_red+"Entered number is incorrect. Please try entering the number from existing "
                                            "numbers"+color_end)
                        else:
                            player1_input = True
                    number_list = FunctionsClass.update_tic_tac_toe(str(player1_number), number_list, player1)
                    FunctionsClass.get_board(number_list)
                    result = FunctionsClass.validate_if_won_or_drawn(number_list)
                    if result == "Won":
                        print(color_purple+"Congratulations. Player 1 has won."+color_end)
                        break
                    elif result == "Drawn":
                        print(color_purple+"Match Drawn"+color_end)
                        break
                    else:
                        turn = 'Player 2'
                else:
                    player2_input = False
                    while not player2_input:
                        player2_number = input("Player2: Enter number 1 to 9: \n")
                        if player2_number not in number_list:
                            print(color_red+"Entered number is incorrect. Please try entering the number from existing "
                                  "numbers"+color_end)
                        else:
                            player2_input = True
                    number_list = FunctionsClass.update_tic_tac_toe(str(player2_number), number_list, player2)
                    FunctionsClass.get_board(number_list)
                    result = FunctionsClass.validate_if_won_or_drawn(number_list)
                    if result == "Won":
                        print(color_purple+"Congratulations. Player 2 has won."+color_end)
                        break
                    elif result == "Drawn":
                        print(color_purple+"Match Drawn"+color_end)
                        break
                    else:
                        turn = 'Player 1'
            if not playgame == 'y' or playgame == 'yes':
                print(color_purple+"Have a Good Day.We hope to see you soon."+color_end)
                break
            if not FunctionsClass.replay():
                print(color_purple+"Have a Good Day.We hope to see you soon."+color_end)
                break

    if __name__ == '__main__':
        play_tic_tac_toe()
