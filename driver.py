from functions_2048 import initialize, display, spawnNewTile, getScore, checkBoardState, move, handle_exit, get_exit_key
import keyboard as kb
import time

# ------------ MAIN ------------
boardState = True

accepted_keys = ["w", "a", "s", "d", "up", "left", "down", "right"]
#initialize the board
board = [[],[],[],[]]
for row in board:
    for i in range(4):
        row.append(0)

initialize(board)

kb.on_release_key("esc", handle_exit, suppress=True)

#outer loop -> game is playing
while boardState:
    display(board)

    #waiting for input
    while True:
        key = kb.read_key().lower()

        if key in accepted_keys:
            boardChanged = move(board, key)
            break
        elif get_exit_key():
            break

    if get_exit_key():
        break
    #after input
    if boardChanged:
        spawnNewTile(board)

    #after receiving input and performing actions
    #sleep prevents accidental duplicate inputs
    time.sleep(0.15)
    boardState = checkBoardState(board)

display(board)

kb.on_release_key("esc", lambda key: None)

print("\nGame Over")
print(f'Your score: {getScore()}')

print("Press any key to exit")
key = kb.read_key(suppress=True)