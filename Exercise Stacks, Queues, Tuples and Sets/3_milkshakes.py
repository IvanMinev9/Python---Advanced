from collections import deque
chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshake = 0

while chocolates and cups_of_milk and milkshake < 5:
    chocolate = chocolates[-1]
    milk = cups_of_milk[0]

    if chocolate <= 0 or milk <= 0:
        if chocolate <= 0:
            chocolates.pop()
        if milk <= 0:
            cups_of_milk.popleft()
        continue

    if chocolate == milk:
        milkshake += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, cups_of_milk)) if cups_of_milk else 'empty'}")
