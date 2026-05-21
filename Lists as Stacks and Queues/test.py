from collections import deque

quantity_water = int(input())
people = deque()

command = input()
while command != 'Start':
    people.append(command)
    command = input()

while command != 'End':
    command = input()
    if command.isdigit():
        person = people.popleft()
        water_needed = int(command)
        if quantity_water >= water_needed:
            quantity_water -= water_needed
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif command.startswith('refill'):
        quantity_water += int(command.split()[1])

print(f'{quantity_water} liters left')
