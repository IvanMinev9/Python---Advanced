expression = input()

brackets = {'(': ')',
            '{': '}',
            '[':']'}

stack = []

for char in expression:
    if char in brackets:
        stack.append(char)
    elif char in brackets.values():
        if not stack:
            print('NO')
            break
        last_open = stack.pop()
        if brackets[last_open] != char:
            print('NO')
            break

else:
    if stack:
        print('NO')
    else:
        print('YES')