import tkinter as tk

root = tk.Tk()

# Khởi tạo bảng game
board = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(tk.Button(root, text=" ", width=10, height=3))
        row[-1].grid(row=i, column=j)
    board.append(row)

players = ["X", "O"]
current_player = 0

def check_win():
    for symbol in players:
        for row in board:
            if all(btn["text"] == symbol for btn in row):
                return symbol
        for col in range(5):
            if all(row[col]["text"] == symbol for row in board):
                return symbol
        if all(board[i][i]["text"] == symbol for i in range(5)):
            return symbol
        if all(board[i][4-i]["text"] == symbol for i in range(5)):
            return symbol
    return None

def make_move(board, symbol):
    while True:
        move = input(f"Nhập vị trí để đặt {symbol} (dạng: row,col): ")
        inputs = move.split(',')

        # Kiểm tra xem người dùng đã nhập đúng hai giá trị chưa
        if len(inputs) != 2:
            print("Vui lòng nhập hai giá trị được phân tách bằng dấu phẩy (,).")
            continue

        row, col = inputs
        row, col = int(row) - 1, int(col) - 1

        if row < 5 and col < 5 and board[row][col] == "-":
            board[row][col] = symbol
            break
        else:
            print("Vị trí không hợp lệ, vui lòng thử lại.")


# Set button commands after board is initialized
for i in range(5):
    for j in range(5):
        board[i][j]["command"] = make_move(i, j)

root.mainloop()
