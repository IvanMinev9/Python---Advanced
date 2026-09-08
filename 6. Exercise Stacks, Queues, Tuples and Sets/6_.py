from collections import deque

strings = deque(input().split())

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

found_colors = []

while strings:

    first = strings.popleft()

    if strings:
        last = strings.pop()
    else:
        last = ''

    first_last = first + last
    last_first = last + first

    if first_last in main_colors or first_last in secondary_colors:
        found_colors.append(first_last)

    elif last_first in main_colors or last_first in secondary_colors:
        found_colors.append(last_first)

    else:
        first = first[:-1]
        last = last[:-1]

        middle = len(strings) // 2

        if first:
            strings.insert(middle, first)

        if last:
            strings.insert(middle, last)

# проверка за secondary colors
result = []

for color in found_colors:

    if color in main_colors:
        result.append(color)

    else:
        needed = secondary_colors[color]

        if needed.issubset(found_colors):
            result.append(color)

print(result)