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

    #

    #

    #
