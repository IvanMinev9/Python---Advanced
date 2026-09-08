from collections import deque

qty_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))
while orders and orders[0] <= qty_food:
    qty_food -= orders.popleft()


if orders:
    print('Orders left:', *orders)
else:
    print(f'Orders complete')