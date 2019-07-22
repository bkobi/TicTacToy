# Funcation for text color
def cprint(string, color):
    colors = ['GRAY','RED','GREEN','YELLOW','BLUE','MAGENTA','CYAN','WHITE','CRIMSON']
    color = color.upper()
    if (color in colors):
        return  ('\033[1;3' + str(colors.index(color)).rstrip() + "m" + str(string) + "\033[1;m")
    else:
        return string
#funcation a winner game or even
def game():
    play = "USER"
    matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    Move = "X"
    counter = 0
    while counter < 9:
        row, col = userMove(matrix,play)
        matrix[row][col] = Move
        if checkrow(matrix,row,Move) or checkcolum(matrix,col,Move) or diagOne(matrix,Move) or diagTwo(matrix,Move):
            #print(cprint("player" + {Move} + "is winner","GREEN"))
            printMat(matrix)
            print(cprint(f'player {Move} is winner',"GREEN"))
            return
        if Move == "X":
            Move = "O"
        else:
            Move = "X"
        if play == "USER":
            play = "COMP"
        else:
            play = "USER"
        counter += 1
    print(cprint(f'Game over, not winner!'),"RED")
#Funcation player
def player():
    if random.randint(0, 1) == 0:
        return 'COMP'
    else:
        return "USER"
#Funcation enter input from player
import random
def userMove(mat,play):
    while True:
        printMat(mat)
        if play == "USER":
            row = input(cprint("pleas enter row number 0-2:", "GREEN"))
            colum = input(cprint("pleas enter colum number 0-2:", "GREEN"))
        if play == "COMP":
            row = random.randint(0,2)
            colum = random.randint(0, 2)
        print(play)

        row = str(row)
        colum = str(colum)
        if row not in ['0', '1', '2']:
            print(f'row input error number must be 0-2')
            continue
        if colum not in ['0', '1', '2']:
            print(cprint("colum input error number must be 0-2","RED"))
            continue
        if mat[int(row)][int(colum)] == ' ':
            return int(row), int(colum)
        else:
            print(f'error mat not empty')
#funcation for check row
def checkrow(mat,row, char):
    if mat[row][0] == char and mat[row][1] == char and mat[row][2] == char:
        return True
    return False
#funcation for check colum
def checkcolum(mat,colum, char):
    if mat[0][colum]  == char and mat[1][colum] == char and mat[2][colum] == char:
        return True
    return False
#funcation to check diagonal line one
def diagOne(mat,char):
    for i in range(3):
        if mat[i][i] != char:
            return False
    return True
#funcation to check diagonal line two
def diagTwo(mat,char):
    for i in range(3):
        if mat[i][2-i] != char:
            return False
    return True
#funncation to print board
def printMat(board):
    size = 3
    noUnderline = "   |" * (size - 1) + " \n"
    underline = "___|" * (size - 1) + "___"
    for row in range(size):
        dataLine = ""
        for col in range(size):
            dataLine += " " + board[row][col] + " |"
        dataLine = dataLine[:-1] + "\n"
        if row == size - 1:
            underline = noUnderline
        print(noUnderline + dataLine + underline)

#main code and a question for player to new game
newgame = True
while newgame:
    game()
    newg = input("do you want new game? press (y/n)")
    while newg != "n" and newg != "y":
        newg = input("do you want new game? press (y/n)")
    if newg == "n":
        newgame = False
