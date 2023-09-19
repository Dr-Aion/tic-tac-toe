board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
coordRef = {
  1: (0, 0),
  2: (0, 1),
  3: (0, 2),
  4: (1, 0),
  5: (1, 1),
  6: (1, 2),
  7: (2, 0),
  8: (2, 1),
  9: (2, 2),
}
def print_board(board):
    for i in board:
        for j in board[0]:
            print(j, end=' ')
        print()
print_board(board)

def isNum(userInput):
    if not userInput.isnumeric():
        print('This is not a number')
        return False
    else: return True

def inRange(userInput):
    if(int(userInput) < 0 or int(userInput) > 10): 
        print('This is not a valid number')
        return False
    else: return True

def taken(userInput):
    coord = int(userInput)
    print(coord)
    pos = coordRef[coord]
    x = pos[0]
    y = pos[1]
    print(x)
    print(y)
    if(board[x][y]) == '_':
        board[x][y] = 'X' 
        print_board(board) 
    else: 
        print('this position is taken, try again')
    
while(True):
    playerInput = input('input a position between 1-9 or q to quit: ')
    if(playerInput == 'q'): break
    if(not isNum(playerInput) or not inRange(playerInput)):
        print('enter a valid number')
    taken(playerInput)
    #if(not taken(playerInput)):

    
