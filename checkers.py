from enum import Enum
CLEAR = lambda: os.system('cls' if os.name == 'nt' else 'clear')
GRID_HEIGHT = 8
GRID_WIDTH = 8

wp = "w"
wq = "W"
ey = '-'
bp = 'b'
bq = 'B'

PLAYERS = Enum("Players", "White Black")

def init_grid():
    """Initialise the new grid"""
    grid = [[ey, bp, ey, bp, ey, bp, ey, bp],
            [bp, ey, bp, ey, bp, ey, bp, ey],
            [ey, bp, ey, bp, ey, bp, ey, bp],
            [bp, ey, bp, ey, bp, ey, bp, ey],
            [ey, ey, ey, ey, ey, ey, ey, ey],
            [ey, ey, ey, ey, ey, ey, ey, ey],
            [ey, wp, ey, wp, ey, wp, ey, wp],
            [wp, ey, wp, ey, wp, ey, wp, ey],
            [ey, wp, ey, wp, ey, wp, ey, wp],
            [wp, ey, wp, ey, wp, ey, wp, ey]]
    return grid

def main():
    """ Entry point """
    print("PY-CHECKERS")
    value_package = dict([("board", init_grid()),("cur_turn", PLAYERS.White)])
    board = init_grid()
    for i in range(8):
        move(value_package, board)
        print_board(board)
        break
    
def print_board(board):
    print("\n      A B C D E F G H")
    for i in range(8):
        print(i, "   |", end="")
        for j in range (8):
            print (board[i][j] + "|", end="")
        print("")
    print("")

def move(value_package, board):
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn:\n")
        print_board(board)
        while True:
            print("Enter movement :", end="")
            print_board(board)
            return move(value_package, board)
    else:
        print("Black's turn:\n")
        value_package["cur_turn"] = PLAYERS.White

main()
