from functions_2048 import initialize, display, spawnNewTile, getScore, checkBoardState, move
import keyboard as kb
import time, sys

# ------------ MAIN ------------
boardState = True

accepted_keys = ["w", "a", "s", "d", "up", "left", "down", "right"]
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

        if key == "esc":
            print("Game exited (escape pressed)")
            print(f"Score: {getScore()}")
            sys.exit(0)
        elif key in accepted_keys:
            boardChanged = move(board, key)
            break

    #after input
    if boardChanged:
        spawnNewTile(board)

    #after receiving input and performing actions
    #sleep prevents accidental duplicate inputs
    time.sleep(0.15)
    boardState = checkBoardState(board)

display(board)

print("\nGame Over")
print(f'Your score: {getScore()}')