import os
from boards import get_empty_board, display_board_5x5
from ships import ship_kuter_coord, ship_destroyer_coord
from menu import game_menu, game_name, instruction, ships_description

unavailable_points = []

players = []

points = {"A1" : (0,0), "A2" : (0,1), "A3" : (0,2), "A4" : (0,3), "A5" : (0,4),
          "B1" : (1,0), "B2" : (1,1), "B3" : (1,2), "B4" : (1,3), "B5" : (1,4),
          "C1" : (2,0), "C2" : (2,1), "C3" : (2,2), "C4" : (2,3), "C5" : (2,4),
          "D1" : (3,0), "D2" : (3,1), "D3" : (3,2), "D4" : (3,3), "D5" : (3,4),
          "E1" : (4,0), "E2" : (4,1), "E3" : (4,2), "E4" : (4,3), "E5" : (4,4),}


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu_choose():
    menu_options = ["1", "2", "3"]
    while True:
        choose_menu = input("Wybierz opcję z menu:\n>")
        if choose_menu in menu_options:
            if choose_menu == "2":
                cls()
                print(instruction)
                print("")
                while True:
                    choose = input("wpisz 'm', aby wrócić do menu:\n>").upper()
                    if choose == "M":
                        cls()
                        start()
                        break
                    else:
                        print("\nnieznana komenda, spróbuj ponownie\n")
                        continue
            elif choose_menu == "3":
                cls()
                print(ships_description)
                print("")
                while True:
                    choose = input("wpisz 'm', aby wrócić do menu:\n>").upper()
                    if choose == "M":
                        cls()
                        start()
                        break
                    else:
                        print("\nnieznana komenda, spróbuj ponownie\n")
                        continue
            elif choose_menu == "1":
                cls()
                start_game()
                break
            break
        else:
            print("Nie ma takie opcji. Wybierz jedną z opcji menu")
            continue

def start():
    print(game_name)
    print(game_menu)
    menu_choose()

def start_game():
    player_number = 1
    while player_number < 3 :
        if player_number == 1:
            player_name = input("wprowadź imię pierwszego gracza: \n> ").upper()
        elif player_number == 2:
            player_name = input("wprowadź imię drugiego gracza: \n> ").upper()
        players.append(player_name)
        cls()
        board = get_empty_board()
        print("Ustaw pierwszy kuter na planszy")
        display_board_5x5(board, player_name)
        ship_kuter_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw drugi kuter na planszy")
        display_board_5x5(board, player_name)

        ship_kuter_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw pierwszy niszczyciel na planszy")
        display_board_5x5(board, player_name)

        ship_destroyer_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw drugi niszczyciel na planszy")
        display_board_5x5(board, player_name)
	
        ship_destroyer_coord(board, player_name, points, unavailable_points)
        cls()
        print("Tak wygląda Twoja plansza:")
        display_board_5x5(board, player_name)
        unavailable_points.clear()
        input("wciśnij ENTER, aby kontynuować")
import os
from boards import get_empty_board, display_board_5x5
from ships import ship_kuter_coord, ship_destroyer_coord
from menu import game_menu, game_name, instruction, ships_description

unavailable_points = []

players = []

points = {"A1" : (0,0), "A2" : (0,1), "A3" : (0,2), "A4" : (0,3), "A5" : (0,4),
          "B1" : (1,0), "B2" : (1,1), "B3" : (1,2), "B4" : (1,3), "B5" : (1,4),
          "C1" : (2,0), "C2" : (2,1), "C3" : (2,2), "C4" : (2,3), "C5" : (2,4),
          "D1" : (3,0), "D2" : (3,1), "D3" : (3,2), "D4" : (3,3), "D5" : (3,4),
          "E1" : (4,0), "E2" : (4,1), "E3" : (4,2), "E4" : (4,3), "E5" : (4,4),}


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def menu_choose():
    menu_options = ["1", "2", "3"]
    while True:
        choose_menu = input("Wybierz opcję z menu:\n>")
        if choose_menu in menu_options:
            if choose_menu == "2":
                cls()
                print(instruction)
                print("")
                while True:
                    choose = input("wpisz 'm', aby wrócić do menu:\n>").upper()
                    if choose == "M":
                        cls()
                        start()
                        break
                    else:
                        print("\nnieznana komenda, spróbuj ponownie\n")
                        continue
            elif choose_menu == "3":
                cls()
                print(ships_description)
                print("")
                while True:
                    choose = input("wpisz 'm', aby wrócić do menu:\n>").upper()
                    if choose == "M":
                        cls()
                        start()
                        break
                    else:
                        print("\nnieznana komenda, spróbuj ponownie\n")
                        continue
            elif choose_menu == "1":
                cls()
                start_game()
                break
            break
        else:
            print("Nie ma takie opcji. Wybierz jedną z opcji menu")
            continue

def start():
    print(game_name)
    print(game_menu)
    menu_choose()

def start_game():
    player_number = 1
    while player_number < 3 :
        if player_number == 1:
            player_name = input("wprowadź imię pierwszego gracza: \n> ").upper()
        elif player_number == 2:
            player_name = input("wprowadź imię drugiego gracza: \n> ").upper()
        players.append(player_name)
        cls()
        board = get_empty_board()
        print("Ustaw pierwszy kuter na planszy")
        display_board_5x5(board, player_name)
        ship_kuter_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw drugi kuter na planszy")
        display_board_5x5(board, player_name)

        ship_kuter_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw pierwszy niszczyciel na planszy")
        display_board_5x5(board, player_name)

        ship_destroyer_coord(board, player_name, points, unavailable_points)
        cls()
        print("Ustaw drugi niszczyciel na planszy")
        display_board_5x5(board, player_name)
	
        ship_destroyer_coord(board, player_name, points, unavailable_points)
        cls()
        print("Tak wygląda Twoja plansza:")
        display_board_5x5(board, player_name)
        unavailable_points.clear()
        input("wciśnij ENTER, aby kontynuować")
        file = open("file1.txt", "w", encoding='utf-8')
        print(board, file=file)
        player_number += 1
        cls()
start()




