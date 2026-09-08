# text = list(input())

# for _ in range(len(text)):
#     print(text.pop(), end='')



# solution with stack

text_new = list(input())

stack = []

for _ in range(len(text_new)):
    stack.append(text_new.pop())

print("".join(stack))