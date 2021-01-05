def possible(y, x, n):
    global board
    #check_in_row
    for i in range(9):
        if board[y][i] == n and x!=i:
            return False
   #check_for_column
    for i in range(9):
        if board[i][x] == n and y!=i:
            return False

   #check for the 3x3 boxes
    p = ((x//3)*3)
    q = ((y//3)*3)
    for i in range(3):
        for j in range(3):
            if board[q+i][p+j] == n and (i,j) != (y,x):
                return False
    return True

def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == '-':
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        if solve():
                            return True

                    board[y][x] = '-'
                return False
    print_board(board)
    print("\n\n\n\n\n")

boardfile = open("file.txt", "r")
list = boardfile.readlines()
board = [["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", "", ""]]
for i in range(9):
    for j in range(9):
        if list[i][j] in '123456789':
            board[i][j] = int(list[i][j])
        else:
            board[i][j] = (list[i][j])
boardfile.close()



print_board(board)
print("\n\n\n\n\n\n")
solve()




