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
    CLEAR()
    print(PY-CHECKERS)
    value_packafe = dict([("board", init_grid()), ("turn_count", 1), ("cur_town", PLAYERS.white)])
    while True:
        move(value_package)
    
def print_board(board)

    print("         A B C D E F G H\n")
    for i in range(GRID_HEIGHT):
        print(i, "   |" end="")
        for j in range (GRID_WIDTH):
            current_cell = board[i][j]
            print (current_cell + "|", end="")
        print("")
    print("")


def check_move_legality(board, tuples)
    return True


def transform_response_into_tuples(response)

    match = re.findall("^([0-9][A-H]){1}$", response)
    l_val1 = ord(match[0][0]) - 48
    l_val2 = ord(match[1][0]) - 48
    r_val1 = ord(match[0][1]) - 65
    r_val2 = ord(match[1][1]) - 65
    return ((l_val1, r_val1), (l_val2, r_val2))


def check_response_syntax

    return False if re.match("^([0-9][A-H]){2}$", response) == None else True


def interpret_response

    if check_response_syntax(response):
        tuples = transform_response_into_tuples(response)
        if check_move_legality(board, tuples):
            return True
        else:
            print("Syntax error")
        return False


def move(value_package)
    print("Turn : ", value_package["turn_count"])
    if value_package["cur_turn"] == PLAYERS.White:
        print("White's turn :\n")
        print_board(value_package["board"])
        while True:
            print("Enter movement :", end="")
            if interpret_response["cur_turn"] = PLAYERS.Black
            value_package["turn_count"] += 1
            break
    else:
        print("Black's turn:\n")
        value_package["cur_turn"] = PLAYERS.White


















        
