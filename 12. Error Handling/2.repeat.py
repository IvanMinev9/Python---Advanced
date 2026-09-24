text = input()

try:
    times = int(input())
except ValueError as err:
    print(f"Variable times must be an integer - {err}")
else:
    print(times * text)