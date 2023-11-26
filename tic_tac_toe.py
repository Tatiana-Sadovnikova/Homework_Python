import random
def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
def get_player_move(board, player_symbol):
    while True:
        move = int(input("Введите номер ячейки для вашего хода (от 1 до 9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = player_symbol
            break
        else:
            print("Некорректный ход. Пожалуйста, выберите свободную ячейку.")
def get_computer_move(board, computer_symbol):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = computer_symbol
            break
def check_win(board, symbol):
    lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == symbol:
            return True
    return False
def main():
    board = [" "] * 9
    player_symbol = "X"
    computer_symbol = "O"
    turn = 0
    while True:
        draw_board(board)
        if turn % 2 == 0:
            get_player_move(board, player_symbol)
        else:
            get_computer_move(board, computer_symbol)
        if check_win(board, player_symbol):
            draw_board(board)
            print("Поздравляю! Вы выиграли!")
            break
        elif check_win(board, computer_symbol):
            draw_board(board)
            print("Компьютер победил. Попробуйте еще раз.")
            break
        elif " " not in board:
            draw_board(board)
            print("Ничья!")
            break
        turn += 1
main()
