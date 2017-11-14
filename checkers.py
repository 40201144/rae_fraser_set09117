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

def main():
    """ Entry point """
    print("PY-CHECKERS")
    value_package = dict([("board", init_grid()),("cur_turn", PLAYERS.White)])
    board = init_grid()
    while True:
      print_board(board)
      move(value_package, board)
      break

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
    
def print_board(board):
    print("\n      0 1 2 3 4 5 6 7")
    for i in range(GRID_HEIGHT):
        print(i, "   |", end="")
        for j in range(GRID_WIDTH):
            print(board[i][j] + "|", end="")
        print("")
    print("")



def move(value_package, board):
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn:\n")
        print_board(board)
        
        init_x = int(input("Please choose target x-coordinate: "))
        init_y = int(input("Please choose target y-coordinate: "))
        end_x = int(input("Please choose a destination x-coordinate: "))
        end_y = int(input("Please choose a destination y-coordinate: "))
        while True:
            print("Enter movement :", end="")
            print_board(board)
        else:
            print("Black's turn:\n")
            value_package["cur_turn"] = PLAYERS.White




main()
