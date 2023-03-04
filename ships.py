def ship_kuter_coord(board, player_name, points, unavailable_points):
    while True:
        print(player_name)
        user_coord = input("Wprowadź współrzędną dla kutra:\n> ").upper()
        if len(user_coord) == 2:
            if user_coord in points:
                coord = points[user_coord]
                x = coord[0]
                y = coord[1]
            else:
                print("Kuter nie może wypłynąć poza obszar Twojej planszy, spróbuj ponownie")
                continue
            if board[x][y] == "░":
                if coord not in unavailable_points:
                    board[x][y] = "•"
                    unavailable_points.extend([((x + 1), y), ((x - 1), y), (x, (y + 1)), (x, (y - 1))])
                    break
                else:
                    print("Zbyt duże ryzyko zderzenia z innym statkiem, wpisz inną współrzędną")
            else:
                print("Tutaj już pływa inny statek, wpisz inną współrzędną")
        else:
            print("Błędna współrzędna, spróbuj ponownie")


def ship_destroyer_coord(board, player_name, points, unavailable_points):
    while True:
        print(player_name)
        user_coord_1 = input("wprowadź pierwszą współrzędną dla niszczyciela:\n> ").upper()
        user_coord_2 = input("wprowadź drugą współrzędną dla niszczyciela:\n> ").upper()
        if len(user_coord_1) == 2 and len(user_coord_2) ==2:
            if user_coord_1 in points and user_coord_2 in points:
                coord_1 = points[user_coord_1]
                coord_2 = points[user_coord_2]
                x1 = coord_1[0]
                y1 = coord_1[1]
                x2 = coord_2[0]
                y2 = coord_2[1]
            else:
                print("Niszczyciel nie może wypłynąć poza obszar Twojej planszy, spróbuj ponownie")
                continue
            if board[x1][y1] == "░" and board[x2][y2] == "░":
                if coord_1 not in unavailable_points and coord_2 not in unavailable_points:
                    if abs(x2-x1) == 1 and y1 == y2 or x1 == x2 and abs(y2-y1)==1:
                        board[x1][y1] = "•"
                        board[x2][y2] = "•"
                        unavailable_points.extend([((x1 + 1), y1), ((x1 - 1), y1), (x1, (y1 + 1)), (x1, (y1 - 1)), ])
                        unavailable_points.extend([((x2 + 1), y2), ((x2 - 1), y2), (x2, (y2 + 1)), (x2, (y2 - 1)), ])
                        break
                    else:
                        print("Nie możesz podzielić statku na pół :-),\nmusisz wpisać dwie sąsiadujące ze sobą współrzędne")
                else:
                    print("Zbyt duże ryzyko zderzenia z innym statkiem, wpisz inne współrzędne")
            else:
                print("Tutaj już pływa inny statek, wpisz inne współrzędne")
        else:
            print("Błędne współrzędne, spróbuj ponownie")