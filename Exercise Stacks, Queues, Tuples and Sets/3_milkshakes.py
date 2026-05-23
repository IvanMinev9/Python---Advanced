from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milk and milkshakes < 5:

    # remove invalid chocolates
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()

    # remove invalid milk
    while milk and milk[0] <= 0:
        milk.popleft()

    if not chocolates or not milk:
        break

    chocolate = chocolates[-1]
    current_milk = milk[0]

    if chocolate == current_milk:
        chocolates.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.append(milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")