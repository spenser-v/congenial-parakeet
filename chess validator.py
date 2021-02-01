
imported_chess_board = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook',
'2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
'3a': ' ', '3b': ' ', '3c': ' ', '3d': ' ', '3e': ' ', '3f': ' ', '3g': ' ', '3h': ' ',
'4a': ' ', '4b': ' ', '4c': ' ', '4d': ' ', '4e': ' ', '4f': ' ', '4g': ' ', '4h': ' ',
'5a': ' ', '5b': ' ', '5c': ' ', '5d': ' ', '5e': ' ', '5f': ' ', '5g': ' ', '5h': ' ',
'6a': ' ', '6b': ' ', '6c': ' ', '6d': ' ', '6e': ' ', '6f': ' ', '6g': ' ', '6h': ' ',
'7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
'8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook'}

legal_chess_board_positions = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
'3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
'5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h', '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
'7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']

legal_chess_pieces = ['wrook', 'wknight', 'wbishop', 'wqueen', 'wking', 'wpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking', 'bpawn', ' ']

piece_list = list(imported_chess_board.values())
position_list = list(imported_chess_board.keys())

w_pieces = 0
b_pieces = 0

for i in piece_list:
    if i[0][0] == 'w':
        w_pieces += 1
    if i[0][0] == 'b':
        b_pieces += 1

def is_valid_chess_board(board):
    #check for white king/black king != 1
    valid_table = True
    if piece_list.count('wking') != 1 or piece_list.count('bking') != 1:
        print('Invalid number of kings.')
        valid_table = False
    #check for too many pieces (>16)
    if w_pieces > 16 or b_pieces > 16:
        print('Too many pieces.')
        valid_table = False
    #check for too many pawns (>8)
    if piece_list.count('wpawn') > 8 or piece_list.count('bpawn') > 8:
        print('Too many pawns.')
        valid_table = False
    #check for illegal notation
    if any(c not in legal_chess_board_positions for c in position_list):
        print('Invalid position input.')
        valid_table = False
    if any(c not in legal_chess_pieces for c in piece_list):
        print('Invalid piece input.')
        valid_table = False

    ##original position check attempt

    ## legal_chess_letter_range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ## legal_chess_number_range = ['1', '2', '3', '4', '5', '6', '7', '8']
    ## for i in position_list:
    ##      if i[0][1] not in legal_chess_letter_range or i[0][0] not in legal_chess_number_range:
    ##          print('invalid position input')
    ##          valid_table = False

    #truth flag
    if valid_table == True:
        print('This board is valid.')
is_valid_chess_board(imported_chess_board)