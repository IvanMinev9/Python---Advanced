# from collections import deque

# materials = [int(x) for x in input().split()]
# magic = deque(int(x) for x in input().split())

# presents = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle'
# }

# crafted = {}

# while materials and magic:

#     # махаме нули
#     if materials[-1] == 0:
#         materials.pop()
#         continue

#     if magic[0] == 0:
#         magic.popleft()
#         continue

#     material = materials.pop()
#     current_magic = magic.popleft()

#     result = material * current_magic

#     if result in presents:
#         toy = presents[result]

#         if toy not in crafted:
#             crafted[toy] = 0

#         crafted[toy] += 1

#     elif result < 0:
#         materials.append(material + current_magic)

#     else:
#         materials.append(material + 15)

# success = (
#     ('Doll' in crafted and 'Wooden train' in crafted)
#     or
#     ('Teddy bear' in crafted and 'Bicycle' in crafted)
# )

# if success:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# for toy in sorted(crafted):
#     print(f"{toy}: {crafted[toy]}")


from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

points = {
    150: "Doll", 
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents = {}

while materials and magic_level:
    craft_magic = materials[-1] * magic_level[0]
    if craft_magic in points:
        new_present = points[craft_magic]
        presents[new_present] = presents.get(new_present, 0) + 1
        materials.pop()
        magic_level.popleft()
    elif craft_magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif craft_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if magic_level[0] == 0:
            magic_level.popleft()
        if materials[-1] == 0:
            materials.pop()
success = (
    ('Doll' in presents and "Wooden train" in presents)
    or 
    ('Teddy bear' in presents and 'Bicycle' in presents)
)
if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

for key, value in sorted(presents.items()):
    print(f'{key}: {value}')



#     presents = Counter() 

#     if craft_magic in points:
#         new_present = points[craft_magic]
#         presents[new_present] += 1