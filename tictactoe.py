import sys

gamedict = {}
for x in range(1, 10):
    gamedict[x] = ' '

player_options = []
for key, value in gamedict.items():
    player_options.append(key)

def initialize_board(player_options):
    board_nums = player_options[::-1]
    player_row3 = create_row(board_nums[:3])
    player_row2 = create_row(board_nums[3:6])
    player_row1 = create_row(board_nums[6:])
    border_row = ['------+-----+------']

    ordered_rows = [player_row1, border_row, player_row2, border_row, player_row3]

    return ordered_rows

def create_row(board_nums):
        row_name = []
        row_name.append('  ')
        row_name.append(board_nums.pop())
        row_name.append(' | ')
        row_name.append(board_nums.pop())
        row_name.append(' | ')
        row_name.append(board_nums.pop())
        row_name.append('  ')

        return row_name

def print_board(gameboard):
    print()
    for x in gameboard:
        print(*x)
    print()

def validate_input():
    ask = None
    try:
        ask = int(input("Where would you like to move? "))
    except ValueError:
        validate_input()
    return ask

def place_player(player_input, boardgame, player):
    for x in range(7):
        if boardgame[0][x] == player_input:
            boardgame[0][x] = player
        elif boardgame[2][x] == player_input:
            boardgame[2][x] = player
        elif boardgame[4][x] == player_input:
            boardgame[4][x] = player

    return boardgame

def check_winner(boardgame):
    # horizontal
    if boardgame[0][1] == boardgame[0][3] and boardgame [0][3] == boardgame[0][5]:
        return boardgame[0][1]
    elif boardgame[2][1] == boardgame[2][3] and boardgame[2][3] == boardgame[2][5]:
        return boardgame[2][1]
    elif boardgame[4][1] == boardgame[4][3] and boardgame[4][3] == boardgame[4][5]:
        return boardgame[4][1]
    # vertical
    elif boardgame[0][1] == boardgame[2][1] and boardgame[2][1] == boardgame[4][1]:
        return boardgame[0][1]
    elif boardgame[0][3] == boardgame[2][3] and boardgame[2][3] == boardgame[4][3]:
        return boardgame[0][3]
    elif boardgame[0][5] == boardgame[2][5] and boardgame[2][5] == boardgame[4][5]:
        return boardgame[0][5]
    #diagnonal
    elif boardgame[0][1] == boardgame[2][3] and boardgame[2][3] == boardgame[4][5]:
        return boardgame[0][1]
    elif boardgame[4][1] == boardgame[2][3] and boardgame[2][3] == boardgame[0][5]:
        return boardgame[4][1]
    else:
        return None

def play():
    boardgame = initialize_board(player_options)

    turn_count = 0
    player = "X"
    remaining_spots = player_options[:]

    print("Welcome to Tic Tac Toe.")
    print_board(boardgame)
    print("The numbers indicate positions on the board.")
    print("You will be prompted to enter which number position you want to place your marker (X or O).")
    
    # Game ends on 9th move
    while turn_count <= 8:
        # Quickest win can only happen in 5 turns
        if turn_count >= 5:
            winner = check_winner(boardgame)
            if winner:
                print(f"Yay {winner} won!")
                
                valid_response = ['Y', 'y', 'N', 'n']
                play_again = input("Do you wish to play again? Y/N ").strip()
                while play_again not in valid_response:
                    play_again = input("Do you wish to play again? Y/N ").strip()
                if play_again.lower() == 'y':
                    print()
                    play()
                else:
                    sys.exit()
        else:
            if player == "X":
                print("Player X's turn!")
                print("\nYou can move to: ", end="")
                print(*remaining_spots)

                make_move = validate_input()
                while make_move not in remaining_spots:
                    print("Sorry, that spot is taken! Try again.")
                    make_move = validate_input()

                boardgame = place_player(make_move, boardgame, player)
                print_board(boardgame)

                remaining_spots.remove(make_move)
                player = "O"
                turn_count += 1

            else:
                print("Player O's turn!")
                print("\nYou can move to: ", end="")
                print(*remaining_spots)

                make_move = validate_input()
                while make_move not in remaining_spots:
                    print("Sorry, that spot is taken! Try again.")
                    make_move = validate_input()

                boardgame = place_player(make_move, boardgame, player)
                print_board(boardgame)

                remaining_spots.remove(make_move)
                player = "X"
                turn_count += 1
play()