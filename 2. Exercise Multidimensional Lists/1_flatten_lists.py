data = input()
matrix = []
numbers = data.split('|')

for nums in reversed(numbers):
    if nums:
        numbers = nums.split()
        matrix.extend(numbers)

print(*matrix)