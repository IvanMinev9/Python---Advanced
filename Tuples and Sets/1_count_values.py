nums = tuple([float(el) for el in input().split()])
data = {}

for element in nums:
    if element not in data:
        data[element] = nums.count(element)

for key, value in data.items():
    print(f'{key} - {value} times')