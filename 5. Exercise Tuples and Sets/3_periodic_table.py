new_set = set()

for _ in range(int(input())):
    for element in input().split():
        new_set.add(element)

print(*new_set, sep='\n')