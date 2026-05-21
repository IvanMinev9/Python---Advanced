from collections import deque

liters_water = int(input())
people = deque()

command = input()
while command != 'Start':
    people.append(command)
    command = input()

while command != 'End':
    command = input()
    if command.isdigit():
      person = people.popleft()
      liters_needed = int(command)
      if liters_water >= liters_needed:
         liters_water -= liters_needed
         print(f'{person} got water')
      else:
         print(f'{person} must wait')
    
    elif command.startswith('refill'):
       liters_water += int(command.split()[1])

print(f'{liters_water} liters left')