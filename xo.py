board = list(range(1,10))
wins_coord = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]
def draw_board():
    print('-----------------') 
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
    print('-----------------')      
def take_input(token):
    while True:
        a = input('введите число для: '+ token)
        if not (a in '123456789'):
            print('введите чило от 1 до 9: ')
            continue
        a = int(a)
        if str(board[a - 1]) in 'xo':
            print('ячейка занята!')
            continue
        board[a - 1] = token
        break
def win():
    for x in wins_coord:
        if (board[x[0]-1]) == (board[x[1]-1]) == (board[x[2]-1]):
            return(True)
    else:
        return False
def main():
    hod = 0
    while True:
        draw_board()
        if hod % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        if hod > 3:
            winnner = win()
            if winnner:
                draw_board()
                print('выиграл!')
                break
        hod += 1
        if hod > 8:
            draw_board()
            print('ничья')
            break
main()