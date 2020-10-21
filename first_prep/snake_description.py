n = int(input())

board_size = [list(input()) for _ in range(n)]


def search_board(board, search):
    for y, row in enumerate(board):
        for x, ch in enumerate(row):
            if ch == search:
                return y, x


snake_pos = search_board(board_size, "S")
print(snake_pos)
