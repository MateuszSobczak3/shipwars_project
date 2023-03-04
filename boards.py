def get_empty_board():
    empty_board = [['░', '░', '░', '░', '░'],
                   ['░', '░', '░', '░', '░'],
                   ['░', '░', '░', '░', '░'],
                   ['░', '░', '░', '░', '░'],
                   ['░', '░', '░', '░', '░']]
    return empty_board

def display_board_5x5(board, player_name):
    print(" ")
    print(" ")
    print("     ", "plansza gracza")
    print("     ", "•", player_name)
    print(" ")
    print("   ", "    1   2   3   4   5")
    print("   ", "  ╔═══╤═══╤═══╤═══╤═══╗")
    print("   ", "A", "║", board[0][0], "│", board[0][1], "│", board[0][2], "│", board[0][3], "│", board[0][4], "║")
    print("   ", "  ╟───┼───┼───┼───┼───╢")
    print("   ", "B", "║", board[1][0], "│", board[1][1], "│", board[1][2], "│", board[1][3], "│", board[1][4], "║")
    print("   ", "  ╟───┼───┼───┼───┼───╢")
    print("   ", "C", "║", board[2][0], "│", board[2][1], "│", board[2][2], "│", board[2][3], "│", board[2][4], "║")
    print("   ", "  ╟───┼───┼───┼───┼───╢")
    print("   ", "D", "║", board[3][0], "│", board[3][1], "│", board[3][2], "│", board[3][3], "│", board[3][4], "║")
    print("   ", "  ╟───┼───┼───┼───┼───╢")
    print("   ", "E", "║", board[4][0], "│", board[4][1], "│", board[4][2], "│", board[4][3], "│", board[4][4], "║")
    print("   ", "  ╚═══╧═══╧═══╧═══╧═══╝")