import keyboard as kb
import random
import time
import copy

#functions modify board in place

#randomly select 2 coordinates, initialize
def initialize(board):
    coords = []
    for row in range(4):
        for col in range(4):
            coords.append((row, col))

    random.shuffle(coords)

    board[coords[0][0]][coords[0][1]], board[coords[1][0]][coords[1][1]] = random.choice([2]*7+[4]), random.choice([2]*7+[4])
    del coords

#return True if the board was changed, false if the board remains unchanged
#all directions follow the same logic
#for input 'w' (move up), parse array from top to bottom. If value at location in array is 0, pass. If value is not 0, shift value
#upward as long as spaces are empty. Once above space is not empty (or edge of the board), check if above space holds same value as
#current space. If values are the same, merge.
def move(board, dir) -> bool:
    original = copy.deepcopy(board)
    merged = []
    if dir == "w": #up
        for r in range(1, 4):
            for c in range(4):
                if board[r][c] != 0:
                    temp = r
                    while temp > 0 and (board[temp-1][c] == 0 or board[temp-1][c] == board[temp][c]):
                        if board[temp-1][c] == 0:
                            board[temp-1][c] = board[temp][c]
                            board[temp][c] = 0
                            temp -= 1
                        elif board[temp-1][c] == board[temp][c] and (temp-1, c) not in merged:
                            board[temp-1][c] *= 2
                            board[temp][c] = 0
                            merged.append((temp-1, c))
                        else:
                            break
                                
    if dir == "a": #left
        for r in range(4):
            for c in range(1, 4):
                if board[r][c] != 0:
                    temp = c
                    while temp > 0 and (board[r][temp-1] == 0 or board[r][temp-1] == board[r][temp]):
                        if board[r][temp-1] == 0:
                            board[r][temp-1] = board[r][temp]
                            board[r][temp] = 0
                            temp -= 1
                        elif board[r][temp-1] == board[r][temp] and (r, temp-1) not in merged:
                            board[r][temp-1] *= 2
                            board[r][temp] = 0
                            merged.append((r, temp-1))
                        else:
                            break

    if dir == "s": #down
        for r in range(2, -1, -1):
            for c in range(4):
                if board[r][c] != 0:
                    temp = r
                    while temp < 3 and (board[temp+1][c] == 0 or board[temp+1][c] == board[temp][c]):
                        if board[temp+1][c] == 0:
                            board[temp+1][c] = board[temp][c]
                            board[temp][c] = 0
                            temp += 1
                        elif board[temp+1][c] == board[temp][c] and (temp+1, c) not in merged:
                            board[temp+1][c] *= 2
                            board[temp][c] = 0
                            merged.append((temp+1, c))
                        else:
                            break

    if dir == "d": #right
        for r in range(4):
            for c in range(2, -1, -1):
                if board[r][c] != 0:
                    temp = c
                    while temp < 3 and (board[r][temp+1] == 0 or board[r][temp+1] == board[r][temp]):
                        if board[r][temp+1] == 0:
                            board[r][temp+1] = board[r][temp]
                            board[r][temp] = 0
                            temp += 1
                        elif board[r][temp+1] == board[r][temp] and (r, temp+1) not in merged:
                            board[r][temp+1] *= 2
                            board[r][temp] = 0
                            merged.append((r, temp+1))
                        else:
                            break

    del merged
    return original != board


#returns false if no moves are available
def checkBoardState(board) -> bool:
    #Checks if any board spaces are empty. If any spaces are empty, a move is available.
    for row in board:
        if 0 in row:
            return True
    #check for available moves by merging
    for r in range(3):
        for c in range(3):
            if board[r][c] == board[r+1][c] or board[r][c] == board[r][c+1]:
                return True
    for r in range(3):
        if board[r][3] == board[r+1][3]:
            return True
    for c in range(3):
        if board[3][c] == board[3][c+1]:
            return True
    return False

#Creates a list of empty coordinates. Selects a random coordinate from the list of empty coords to create a new tile. 
def spawnNewTile(board):
    empty = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                empty.append((row, col))
    if len(empty) > 0:
        coord = random.choice(empty)
        board[coord[0]][coord[1]] = random.choice([2]*6+[4])
        del coord
    del empty

def display(board):
    for row in board:
        for val in row:
            if val == 0:
                val = "-"
            print(f"{val}\t", end='')
        print()
    print("\n")

#score is the sum of all tiles
def findScore(board) -> int:
    score = 0
    for row in board:
        for val in row:
            score += val

    return score



# ------------ MAIN ------------
boardState = True

#initialize the board
board = [[],[],[],[]]
for row in board:
    for i in range(4):
        row.append(0)

initialize(board)

#outer loop -> game is playing
while boardState:
    display(board)

    #waiting for input
    while True:
        key = kb.read_key().lower()

        if key == "w" or key == "a" or key == "s" or key == "d":
            boardChanged = move(board, key)
            break

    #after input
    if boardChanged:
        spawnNewTile(board)

    #after receiving input and performing actions
    #sleep prevents accidental duplicate inputs
    time.sleep(0.2)
    boardState = checkBoardState(board)

display(board)

print("\nGame Over")
print(f'Your score: {findScore(board)}')
