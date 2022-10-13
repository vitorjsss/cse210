from operator import truediv


def main():
    player = "x"
    square_1 = 1
    square_2 = 2
    square_3 = 3
    square_4 = 4
    square_5 = 5
    square_6 = 6
    square_7 = 7
    square_8 = 8
    square_9 = 9
    end = False
    draw_board(square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9)
    while end == False:
        movement = True
        square_number = int(input(f"{player}'s turn to choose a square (1-9): "))
        if square_number > 0 and square_number <= 9:
            if square_number == 1 and square_1 == 1:
                square_1 = player
            elif square_number == 2 and square_2 == 2:
                square_2 = player
            elif square_number == 3 and square_3 == 3:
                square_3 = player
            elif square_number == 4 and square_4 == 4:
                square_4 = player
            elif square_number == 5 and square_5 == 5:
                square_5 = player
            elif square_number == 6 and square_6 == 6:
                square_6 = player
            elif square_number == 7 and square_7 == 7:
                square_7 = player
            elif square_number == 8 and square_8 == 8:
                square_8 = player
            elif square_number == 9 and square_9 == 9:
                square_9 = player
            else:
                print("Square already chosen! Try again")
                movement = False
            if movement == True:
                winner = checking_winner(player, square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9)
                if winner == True:
                    draw_board(square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9)
                    end = True
                else:
                    if square_1 != 1 and square_2 != 2 and square_3 != 3 and square_4 != 4 and square_5 != 5 and square_6 != 6 and square_7 != 7 and square_8 != 8 and square_9 != 9:
                        draw_board(square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9)
                        print("It's a tie!")
                        end = True
                    else:
                        if player == "x":
                            player = "o"
                        elif player == "o":
                            player = "x"
                        draw_board(square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9)
        else:
            print("Invalid digit. Try again")

def draw_board(blank_1, blank_2, blank_3, blank_4, blank_5, blank_6, blank_7, blank_8, blank_9):
    print(f"{blank_1}|{blank_2}|{blank_3}\n-+-+-\n{blank_4}|{blank_5}|{blank_6}\n-+-+-\n{blank_7}|{blank_8}|{blank_9}\n")

def checking_winner(player, value_1, value_2, value_3, value_4, value_5, value_6, value_7, value_8, value_9):
    if value_1 == value_2 and value_1 == value_3:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_1 == value_4 and value_1 == value_7:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_1 == value_5 and value_1 == value_9:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_2 == value_5 and value_2 == value_8:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_3 == value_6 and value_3 == value_9:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_4 == value_5 and value_4 == value_6:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_7 == value_5 and value_7 == value_3:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    elif value_7 == value_8 and value_7 == value_9:
        print(f"Player {player} won!")
        print("Good game! Thanks for playing!")
        return True
    else:
        return False

if __name__ == "__main__":
    main()