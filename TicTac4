def cprint(string, color):
    colors = ['GRAY','RED','GREEN','YELLOW','BLUE','MAGENTA','CYAN','WHITE','CRIMSON']
    color = color.upper()
    if (color in colors):
        return  ('\033[1;3' + str(colors.index(color)).rstrip() + "m" + str(string) + "\033[1;m")
    else:
        return string
def game():
    matrix = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
    Move = "X"
    counter = 0
    while counter < 12:
        row, col = userMove(matrix)
        matrix[row][col] = Move
        if checkrow(matrix,row,Move) or checkcolum(matrix,col,Move) or diagOne(matrix,Move) or diagTwo(matrix,Move):
            printMat(matrix)
            print(f'player {Move} is winner')
            return
        if Move == "X":
            Move = "O"
        else:
            Move = "X"
        counter += 1
    print(f'game over draw!')
def userMove(mat):
    while True:
        printMat(mat)
        row = input(cprint("pleas enter row number 0-3:","YELLOW"))
        colum = input(cprint("pleas enter colum number 0-3:","YELLOW"))
        if row not in ['0', '1', '2','3']:
            print(cprint("row input error number must be 0-3","RED"))
            continue
        if colum not in ['0', '1', '2','3']:
            print(cprint("colum input error number must be 0-3","RED"))
            continue
        if mat[int(row)][int(colum)] == ' ':
            return int(row), int(colum)
        else:
            print(cprint("error mat not empty","RED"))
def checkrow(mat,row, char):
    if mat[row][0] == char and mat[row][1] == char and mat[row][2] == char and mat[row][3] == char:
        return True
    return False
def checkcolum(mat,colum, char):
    if mat[0][colum]  == char and mat[1][colum] == char and mat[2][colum] == char and mat[3][colum] == char:
        return True
    return False
def diagOne(mat,char):
    for i in range(4):
        if mat[i][i] != char:
            return False
    return True
def diagTwo(mat,char):
    for i in range(4):
        if mat[i][3-i] != char:
            return False
    return True
def printMat(board):
    size = 4
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
newgame = True
while newgame:
    game()
    newg = input(cprint("do you want new game? press (y/n)","GREEN"))
    while newg != "n" and newg != "y":
        newg = input(cprint("do you want new game? press (y/n)","GREEN"))
    if newg == "n":
        newgame = False
