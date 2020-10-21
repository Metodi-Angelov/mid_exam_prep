from functools import reduce
from math import floor

# input examp: 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
    "*": lambda a, b: a * b,
}

user_input = input().split()

current_num = []
for elm in user_input:
    if elm.lstrip("-").isdigit():
        current_num.append(int(elm))
    else:
        fn = reduce(operations[elm], current_num)
        current_num.clear()
        current_num.append(floor(fn))

print(current_num[0])
