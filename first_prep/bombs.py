from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs_quantity = {
    "Cherry Bombs": [60, 0],
    "Datura Bombs": [40, 0],
    "Smoke Decoy Bombs": [120, 0],
}

while True:
    if 0 >= len(bomb_casings) or 0 >= len(bomb_effects):
        print("You don't have enough materials to fill the bomb pouch.")
        break

    elif bombs_quantity["Datura Bombs"][1] >= 3 <= bombs_quantity["Cherry Bombs"][1] and \
            bombs_quantity["Smoke Decoy Bombs"][1] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    if current_casing < 0:
        bomb_effects.appendleft(current_effect)
        continue
    total = current_casing + current_effect
    if total == bombs_quantity["Datura Bombs"][0]:
        bombs_quantity["Datura Bombs"][1] += 1
    elif total == bombs_quantity["Cherry Bombs"][0]:
        bombs_quantity["Cherry Bombs"][1] += 1
    elif total == bombs_quantity["Smoke Decoy Bombs"][0]:
        bombs_quantity["Smoke Decoy Bombs"][1] += 1
    else:
        bomb_casings.append(current_casing - 5)
        bomb_effects.appendleft(current_effect)

if len(bomb_effects) > 0:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if len(bomb_casings) > 0:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for k in bombs_quantity.keys():
    print(f"{k}: {bombs_quantity[k][1]}")