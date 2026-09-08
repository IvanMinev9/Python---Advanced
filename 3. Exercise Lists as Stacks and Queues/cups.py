from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

water_wated = 0

while cups and bottles:
    curr_cup = cups[0]
    while curr_cup > 0:
        curr_bottle = bottles.pop()
        curr_cup -= curr_bottle

    water_wated -= curr_cup
    cups.popleft()

if not cups:
    print("Bottles:", *bottles)
if not bottles:
    print("Cups:", *cups)

print(f"Wasted litters of water: {water_wated}")
