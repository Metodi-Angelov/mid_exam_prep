# Input example:
# 4
# . . p .
# . . . .
# . . t .
# t . . .
# 4
# shoot down 2
# move down 2
# move left 2
# shoot down 3


def move(delta_x, delta_y, pos):
    global plane_position, total_targets
    x, y = plane_position
    new_x = x + delta_x
    new_y = y + delta_y
    if new_x > (battlefield_size - 1) or new_x < 0 or new_y > (battlefield_size - 1) or new_y < 0:
        return
    elif pos == "move":
        if battlefield[new_x][new_y] not in ("x", "t"):
            battlefield[x][y] = "."
            battlefield[new_x][new_y] = "p"
            plane_position = (new_x, new_y)
    elif pos == "shoot":
        if battlefield[new_x][new_y] == "t":
            targets_position.pop()
        battlefield[new_x][new_y] = "x"


battlefield_size = int(input())
battlefield = []
plane_position = tuple()
targets_position = []
total_targets = 0

for x in range(battlefield_size):
    line = input().split()
    for y in range(battlefield_size):
        if line[y] == "p":
            plane_position = (x, y)
        elif line[y] == "t":
            targets_position.append((x, y))
            total_targets += 1
    battlefield.append(line)

num_of_commands = int(input())

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for _ in range(num_of_commands):
    if len(targets_position) == 0:
        break
    command = input().split()
    cmd = command[0]
    direction = command[1]
    add = int(command[2])

    pos = "move" if cmd == "move" else "shoot"
    dic = movements[direction]
    move(dic[0] * add, dic[1] * add, pos)

if len(targets_position) <= 0:
    print(f"Mission accomplished! All {total_targets} targets destroyed.")
else:
    print(f"Mission failed! {len(targets_position)} targets left.")

print("\n".join([" ".join(row) for row in battlefield]))
