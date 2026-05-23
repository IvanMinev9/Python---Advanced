from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
sumbols = deque(input().split())

honey = 0
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operators[sumbols[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        sumbols.popleft()
    else:
        nectar.pop()

print(f'Total honey made: {honey}')

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")