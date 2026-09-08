matrix = int(input())
nums = []

for _ in range(matrix):
    nums.extend([int(x) for x in input().split(", ")])

print(nums)