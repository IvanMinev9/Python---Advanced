from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbol = deque(input().split())

honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b, 
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while nectar and working_bees:
    if nectar[-1] >= working_bees[0]:
        honey += abs(operators[symbol[0]](working_bees[0], nectar[-1]))
        working_bees.popleft()
        nectar.pop()
        symbol.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if nectar:
    print(f'Nectar left: {", ".join(map(str, nectar))}')
if working_bees:
    print(f'Bees left: {", ".join(map(str, working_bees))}')
