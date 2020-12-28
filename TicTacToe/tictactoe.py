# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

# 0 = not taken
# 1 = X
# 2 = 0

square1 = 0
square2 = 0
square3 = 0
square4 = 0
square5 = 0
square6 = 0
square7 = 0
square8 = 0
square9 = 0

current_player = 1

# loop 9 times
for go in range (9):
    # draw board 
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9

    row = ""
    if square1 == 0:
        row = row + "1"
    elif square1 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square2 == 0:
        row = row + "2"
    elif square2 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square3 == 0:
        row = row + "3"
    elif square3 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    print(row)
    print("-----")
    
    row = ""
    if square4 == 0:
        row = row + "4"
    elif square4 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square5 == 0:
        row = row + "5"
    elif square5 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square6 == 0:
        row = row + "6"
    elif square6 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    print(row)
    print("-----")

    row = ""
    if square7 == 0:
        row = row + "7"
    elif square7 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square8 == 0:
        row = row + "8"
    elif square8 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    row = row + "|"

    if square9 == 0:
        row = row + "9"
    elif square9 == 1:
        row = row + "X"
    else: 
        row = row + "0"
    print(row)
    print("")


    # get player input
    if current_player == 1:
        print("Player X' turn")
    else:
        print("Player O's turn")
    position = input("Enter the square number you want ")

    if position == "1":
        square1 = current_player
    elif position == "2":
        square2 = current_player
    elif position == "3":
        square3 = current_player
    elif position == "4":
        square4 = current_player
    elif position == "5":
        square5 = current_player
    elif position == "6":
        square6 = current_player
    elif position == "7":
        square7 = current_player
    elif position == "8":
        square8 = current_player
    elif position == "9":
        square9 = current_player
    
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    

    # check for winner
    winner = 0

    #rows
    if (square1 != 0) and (square1 == square2 == square3):
        # win
        winner = square1
        break
    elif (square4 != 0) and (square4 == square5 == square6):
        # win
        winner = square4
        break
    elif (square7 != 0) and (square7 == square8 == square9):
        # win
        winner = square7
        break

    #coloumns
    elif (square1 != 0) and (square1 == square4 == square7):
        # win
        winner = square1
        break
    elif (square2 != 0) and (square2 == square5 == square8):
        # win
        winner = square2
        break
    elif (square3 != 0) and (square3 == square6 == square9):
        # win
        winner = square3
        break

    #diagonals
    elif (square1 != 0) and (square1 == square5 == square9):
        # win
        winner = square1
        break
    elif (square3 != 0) and (square3 == square5 == square7):
        # win
        winner = square3
        break

    # end loop

# winner has the winning player or 0

# draw board 
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

row = ""
if square1 == 0:
    row = row + "1"
elif square1 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square2 == 0:
    row = row + "2"
elif square2 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square3 == 0:
    row = row + "3"
elif square3 == 1:
    row = row + "X"
else: 
    row = row + "0"
print(row)
print("-----")

row = ""
if square4 == 0:
    row = row + "4"
elif square4 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square5 == 0:
    row = row + "5"
elif square5 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square6 == 0:
    row = row + "6"
elif square6 == 1:
    row = row + "X"
else: 
    row = row + "0"
print(row)
print("-----")

row = ""
if square7 == 0:
    row = row + "7"
elif square7 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square8 == 0:
    row = row + "8"
elif square8 == 1:
    row = row + "X"
else: 
    row = row + "0"
row = row + "|"

if square9 == 0:
    row = row + "9"
elif square9 == 1:
    row = row + "X"
else: 
    row = row + "0"
print(row)
print("")

if winner == 0:
    print("DRAW")
elif winner == 1:
    print("X HAS WON")
else:
    print("O HAS WON")
