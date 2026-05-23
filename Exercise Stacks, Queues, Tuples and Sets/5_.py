from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted = {}

while materials and magic:

    # махаме нули
    if materials[-1] == 0:
        materials.pop()
        continue

    if magic[0] == 0:
        magic.popleft()
        continue

    material = materials.pop()
    current_magic = magic.popleft()

    result = material * current_magic

    if result in presents:
        toy = presents[result]

        if toy not in crafted:
            crafted[toy] = 0

        crafted[toy] += 1

    elif result < 0:
        materials.append(material + current_magic)

    else:
        materials.append(material + 15)

success = (
    ('Doll' in crafted and 'Wooden train' in crafted)
    or
    ('Teddy bear' in crafted and 'Bicycle' in crafted)
)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy in sorted(crafted):
    print(f"{toy}: {crafted[toy]}")