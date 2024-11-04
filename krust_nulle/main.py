SIZE_OF_FIELLD = 3

game_field = [

    ['','',''],
    ['','','']
    ['','','']

]

player_name = ['player lst', 'player 2nd']

row_num = 0
col_num = 0


def show_game_rules():
    pass


def show_menu():
    pass


def show_player_message(plr_num : int):
    print()
    print(player_name[plr_num],'symbol: ' , 'x' if plr_num == 0 else '0')

    if plr_num == 0 :
        print(player_name[plr_num],'symbol: x')

    else:
        print(player_name[plr_num],'symbol: 0')

    
def chk_cell(row_num : int, cal_num: int, plr_sym : str):
        pass


def user_input(plr_num2 : int):
     global row_num
     global col_num

     if plr_num2 == 0:
          plr_sym = 'x'
    
     else:
          per_sym = '0'

     row_num = int(input('input row number from 0 to ' + str(SIZE_OF_FIELLD - 1) + 'include: '))

     col_num = int(input('input row number from 0 to ' + str(SIZE_OF_FIELLD - 1) + 'include: '))

     chk_cell(row_num, col_num, plr_sym)

     #with while


def show_field(sz : int):
     for row in range(sz):
          for col in range(sz):
               print(game_field[row][col], end='')
               print()


def game_field_change(plr_num3 : int):
     game_field[row_num][col_num] = 'x' if plr_num3 == 0 else '0'


def start_game(gsize : int):
     show_field(gsize)


def chk_winner(plr_num4 : int):
     global game_over 

     game_over = True


def play_game():
    show_player_message(0)
    user_input(0)
    game_field_change(0)
    chk_winner(0)

    show_field(SIZE_OF_FIELLD)
    show_player_message(1)
    user_input(0)
    game_field_change(0)
    chk_winner(0)

    show_field(SIZE_OF_FIELLD)


def main(arguments):
     start_game(SIZE_OF_FIELLD)
     while not game_over:
          play_game()
          print('Game Over')
          return 0
     
if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))     













     


        