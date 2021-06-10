import os

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
win=1
draw=-1
running=0
stop=1
game=running
mark='X'

def ticBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

def position(x):
    if(board[x]==' '):
        return True
    else:
        return False

def winStatus():
    global game
    #Hozrizontal win condition
    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        game=win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        game=win
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        game=win
    
    #Vertical win condition
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        game=win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        game=win
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        game=win

    #Diagnol Win conditions
    elif(board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
        game=win
    elif(board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
        game=win
    
    #Game draw condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game=draw
    
    else:
        game=running

while(game==running):
    os.system('cls')
    ticBoard()
    if(player % 2 !=0):
        print("Player 1, play your chance")
        mark='X'
    else:
        print('Palyer 2,play your chance')
        mark='O'
    choice=int(input("Enter the position number (1 to 9) where you want to enter the mark:"))
    if(position(choice)):
        board[choice]=mark
        player=player+1
        winStatus()

os.system('cls')
ticBoard()
if(game==draw):
    print("Game draw")
elif(game==win):
    player=player-1
    if(player %2 !=0):
        print('Player 1 wins this match')
    else:
        print('Player 2 wins the match')