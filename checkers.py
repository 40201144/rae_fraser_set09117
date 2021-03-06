from enum import Enum
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8

wp = "w"
wk = "W"
ey = '-'
bp = 'b'
bk = 'B'
wpt = 12 #Running total of white pieces
bpt = 12 #Running total of Black pieces
     
PLAYERS = Enum("Players", "White Black")

def main():
    print("-Checkers-\n--GAME ON--")
    value_package = dict([("board", init_grid()),("cur_turn", PLAYERS.White)])
    board = init_grid()
    while True:
      print_board(board)
      move(value_package, board, bpt, wpt)
      break

#Defining the grid
def init_grid():
    """Initialise the new grid"""
    grid = [[ey, bp, ey, bp, ey, bp, ey, bp],
            [bp, ey, bp, ey, bp, ey, bp, ey],
            [ey, bp, ey, bp, ey, bp, ey, bp],
            [ey, ey, ey, ey, ey, ey, ey, ey],
            [ey, ey, ey, ey, ey, ey, ey, ey],
            [wp, ey, wp, ey, wp, ey, wp, ey],
            [ey, wp, ey, wp, ey, wp, ey, wp],
            [wp, ey, wp, ey, wp, ey, wp, ey]]
    return grid

#Printing the board
def print_board(board):
    print("\n      0 1 2 3 4 5 6 7")
    for i in range(GRID_HEIGHT):
        print(i, "   |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("")



def move(value_package, board, bpt, wpt):
    #White's turn
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn:\n")
        
        #Get starting coord
        init_x = int(input("Please choose target x-coordinate: "))
        init_y = int(input("Please choose target y-coordinate: "))
        
        #Define ruleset for starting coord
        if board[init_y][init_x] == ey:
            print("There is no piece here to move")
            return move(value_package, board, bpt, wpt)
        if board[init_y][init_x] == bp:
            print("This is not one of your pieces")
            return move(value_package, board, bpt, wpt)
        if board[init_y][init_x] == bk:
            print("This is not one of your pieces")
            return move(value_package, board, bpt, wpt)

        #Get destination coord
        end_x = int(input("Please choose a destination x-coordinate: "))
        end_y = int(input("Please choose a destination y-coordinate: "))

        #Setting a middle value number -- for capping a piece
        mid_x = abs(init_x + end_x) // 2
        mid_y = abs(init_y + end_y) // 2
        
        #Define ruleset for destination coord
        if board[end_y][end_x] == bp:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == wp:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == bk:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == wk:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)

        else:
            
            #Capture a piece           
            if board[mid_y][mid_x] == bp or board[mid_y][mid_x] == bk:
                board[end_y][end_x] = wp
                board[init_y][init_x] = ey
                board[mid_y][mid_x] = ey
                bpt = bpt -1                
                value_package["cur_turn"] = PLAYERS.Black
                print_board(board)
                print ("Black pieces remaining:", bpt)
                if (bpt == 0):
                    print ("Whites won")
                    quit()
                else:
                    return move(value_package, board, bpt, wpt)

            #Checking distance
            if end_x > init_x + 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_x < init_x - 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_y > init_y + 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_y < init_y - 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            #Check direction
            if board[init_x] == board[end_x]:
                print("You can not move vertically")
                return move(value_package, board, bpt, wpt)
            
            if board[init_y] == board[end_y]:
                print("You can not move Horizontally")
                return move(value_package, board, bpt, wpt)
                        
            else:
                #Move the piece
                board[init_y][init_x] = ey
                board[end_y][end_x] = wp
                print_board(board)
                value_package["cur_turn"] = PLAYERS.Black
                return move(value_package, board, bpt, wpt)

            
    #Black's turn
    
    if value_package["cur_turn"] == PLAYERS.Black:
        print("Black's turn:\n")
        
        #Get starting coord
        init_x = int(input("Please choose target x-coordinate: "))
        init_y = int(input("Please choose target y-coordinate: "))
        
        #Define ruleset for starting coord
        if board[init_y][init_x] == ey:
            print("There is no piece here to move")
            return move(value_package, board, bpt, wpt)
        if board[init_y][init_x] == wp:
            print("This is not one of your pieces")
            return move(value_package, board, bpt, wpt)
        if board[init_y][init_x] == wk:
            print("This is not one of your pieces")
            return move(value_package, board, bpt, wpt)

        #Get destination coord
        end_x = int(input("Please choose a destination x-coordinate: "))
        end_y = int(input("Please choose a destination y-coordinate: "))


        #Setting a middle value number -- for capping a piece
        mid_x = abs(init_x + end_x) // 2
        mid_y = abs(init_y + end_y) // 2
        
        #Define ruleset for destination coord
        if board[end_y][end_x] == bp:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == wp:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == bk:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        if board[end_y][end_x] == wk:
            print("This coordinate is currently occupied")
            return move(value_package, board, bpt, wpt)
        
        else:
            
            #Capturing a piece
            if board[mid_y][mid_x] == wp or board[mid_y][mid_x] == wk:
                board[init_y][init_x] = ey
                board[end_y][end_x] = bp
                board[mid_y][mid_x] = ey
                wpt = wpt -1                
                value_package["cur_turn"] = PLAYERS.White
                print_board(board)
                print ("White pieces remaining: ", wpt)
                if (wpt == 0):
                    print ("Blacks won")
                    quit()
                else:
                    return move(value_package, board, bpt, wpt)

            #Checking distance
            if end_x > init_x + 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_x < init_x - 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_y > init_y + 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            if end_y < init_y - 2:
                print("Can not move that far away")
                return move(value_package, board, bpt, wpt)

            #Checking direction
            if board[init_x] == board[end_x]:
                print("You can not move vertically")
                return move(value_package, board, bpt, wpt)
            
            if board[init_y] == board[end_y]:
                print("You can not move Horizontally")
                return move(value_package, board, bpt, wpt)            
                        
            else:
                #Moving a piece
                board[init_y][init_x] = ey
                board[end_y][end_x] = bp
                print_board(board)
                value_package["cur_turn"] = PLAYERS.White
                return move(value_package, board, bpt, wpt)
        
main()






















