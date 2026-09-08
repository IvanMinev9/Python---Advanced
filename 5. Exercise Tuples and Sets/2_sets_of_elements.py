num1, num2 = map(int, input().split())
n_set = {input() for _ in range(num1)}
m_set = {input() for _ in range(num2)}

# for _ in range(num1):
#     n_set.add(input())

# for _ in range(num2):
#     m_set.add(input())

result = n_set.intersection(m_set)

print(*result, sep='\n')