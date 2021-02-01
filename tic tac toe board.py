tic_tac_toe_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
turn = 'X'
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#def check_win(board):

for i in range(9):
    print_board(tic_tac_toe_board)
    print('Player ' + turn + ': Enter move.')
    move = input()
    tic_tac_toe_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    #if i >= 5:
    #    check_win(tic_tac_toe_board)
print_board(tic_tac_toe_board)