number_commands = int(input())
parking = set()

for _ in range(number_commands):
    direction, licence_plate = input().split(', ')
    if direction == 'IN':
        parking.add(licence_plate)
    elif direction == 'OUT':
        parking.remove(licence_plate)

if not parking:
    print('Parking Lot is Empty')

for cars in parking:
    print(cars)