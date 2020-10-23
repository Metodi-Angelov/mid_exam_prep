from collections import deque

males = [int(n) for n in input().split() if int(n) > 0]
females = deque([int(n) for n in input().split() if int(n) > 0])

total_matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]
    if current_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
    elif current_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif current_male == current_female:
        total_matches += 1
        males.pop()
        females.popleft()
    elif current_male != current_female:
        males.append(males.pop() - 2)
        females.popleft()
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {total_matches}")
print(f"Males left: {'none' if not males else ', '.join([str(el) for el in reversed(males)])}")
print(f"Females left: {'none' if not females else ', '.join([str(el) for el in females])}")
