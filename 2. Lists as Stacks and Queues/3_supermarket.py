from collections import deque

queue = deque()

while True:
    lines = input()

    if lines == "End":
        break
    elif lines == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(lines)

print(f'{len(queue)} people remaining.')