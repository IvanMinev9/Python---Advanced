number_guests = int(input())
collector = set()

for _ in range(number_guests):
    reservetion = input()
    collector.add(reservetion)

reservetion = input()


while reservetion != 'END':
    collector.remove(reservetion)
    reservetion = input()

print(len(collector))
sorted_reser = sorted(collector)

for resert in sorted_reser:
    print(resert)