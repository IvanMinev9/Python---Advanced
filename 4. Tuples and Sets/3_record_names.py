number_times = int(input())
unique = set()

for _ in range(number_times):
    names = input()
    unique.add(names)
for name in unique:
    print(name)