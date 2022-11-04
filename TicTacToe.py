def show_board(board):
    for i in board:
        for j in i:
            print(j.center(20,' '),end=' ')
        print('\n')
# show_board(board)
def choice(n):
    x={1:'00',2:'01',3:'02',4:'10',5:'11',6:'12',7:'20',8:'21',9:'22'}
    for i,j in x.items():
        if i==n:
            return x[i]
def board_fill(board):
    for i in board:
        for j in i:
            if j in ['1','2','3','4','5','6','7','8','9']:
                return False
    return True
def player_won(board):
    if (board[0][0]==board[1][1]==board[2][2]):
        return True
    elif (board[0][2]==board[1][1]==board[2][0]):
        return True
    else:
        for i in range(len(board)):
            if board[i][0]==board[i][1]==board[i][2]:
                return True
            elif board[0][i]==board[1][i]==board[2][i]:
                return True
    return False
import random
k=random.randint(0,1)
def positon_vacant(board,r,c):
    if board[r][c] in ['X','O']:
        return False
    else:
        return True

def position(board,r,c,player):
    board[r][c]=player
    return board
def swap(player):
    return 'X' if player=='O' else 'O'

#final code
game=True

board=[['1','2','3'],['4','5','6'],['7','8','9']]
import random
k=random.randint(0,1)

player='X' if k==1 else 'O'
while game:
    i=True
    print(f'player {player} turn')
    show_board(board)
    while True:
        print('Enter the number :')
        x=choice(int(input()))
        row,column=int(x[0]),int(x[1])
        k=positon_vacant(board,row,column)
        if k:
            break
        print('Place Occupied, Try Another One')
    board=position(board,row,column,player)
    if player_won(board):
        print(f'{player} player wins the game')
        m=input('Do you want to play again? Y | N:').upper()
        if m=='Y':
            board=[['1','2','3'],['4','5','6'],['7','8','9']]
        else:
            game=False
            break
    elif board_fill(board):
        print('The Board is full')
        m=input('Do you want to play again? Y | N:').upper()
        if m=='Y':
            board=[['1','2','3'],['4','5','6'],['7','8','9']]
        else:
            game=False
            break
    player=swap(player)
show_board(board)