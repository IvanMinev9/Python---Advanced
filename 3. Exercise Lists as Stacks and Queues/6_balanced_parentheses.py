experssion = input()

brackets = {"(": ")",
            "[": "]",
            "{": "}"}

stack = []

for ch in experssion:
    if ch in brackets:
        stack.append(ch)
    elif ch in brackets.values():
        if not stack:
            print("NO")
            break
        last_opening = stack.pop()
        if brackets[last_opening] != ch:
            print("NO")
            break

else:
    if stack:
        print("NO")
    else:
        print("YES")