clothes = list(map(int, input().split()))
racks_cap = int(input())

racks_used = 0

while clothes:
    racks_used += 1
    curr_rack = racks_cap
    while clothes and curr_rack >= clothes[-1]:
        curr_rack -= clothes.pop()

print(racks_used)