first_sequences = set(int(x) for x in input().split())
second_sequences = set(int(x) for x in input().split())

for _ in range(int(input())):
    line = input().split()
    command = f'{line[0]} {line[1]}'
    numbers = [int(x) for x in line[2:]]

    if command == 'Add First':
        first_sequences.update(numbers)
    elif command == 'Add Second':
        second_sequences.update(numbers)
    elif command == 'Remove First':
        first_sequences.difference_update(numbers)
    elif command == 'Remove Second':
        second_sequences.difference_update(numbers)
    elif command == 'Check Subset':
        print(first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences))

print(*sorted(first_sequences), sep=', ')
print(*sorted(second_sequences), sep=', ')