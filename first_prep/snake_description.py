n = int(input())

board_size = [list(input()) for _ in range(n)]


def search_board(board, search):
    for y, row in enumerate(board):
        for x, ch in enumerate(row):
            if ch == search:
                return y, x


snake_pos = search_board(board_size, "S")
game_over = False
eaten_food = 0


def move(dy, dx):
    global snake_pos, game_over, eaten_food
    y, x = snake_pos
    board_size[y][x] = "."
    new_y = y + dy
    new_x = x + dx
    if new_y > (n - 1) or new_y < 0 or new_x > (n - 1) or new_x < 0:
        game_over = True
        print("Game over!")
        print(f"Food eaten: {eaten_food}")
        return
    pos = board_size[new_y][new_x]
    if pos == "B":
        board_size[new_y][new_x] = "."
        new_y, new_x = search_board(board_size, "B")
    elif pos == "*":
        board_size[new_y][new_x] = "."
        eaten_food += 1
        if eaten_food == 10:
            print("You won! You fed the snake.")
            print(f"Food eaten: {eaten_food}")
            game_over = True
    board_size[new_y][new_x] = "S"
    snake_pos = (new_y, new_x)


def print_board():
    print("\n".join(["".join(row) for row in board_size]))


movement = {
    "up": lambda: move(-1, 0),
    "down": lambda: move(1, 0),
    "right": lambda: move(0, 1),
    "left": lambda: move(0, -1),
}

while not game_over:
    cmd = input()
    fn_move = movement[cmd]
    fn_move()


print_board()
