def negative_positive(*args):
    negative_sum = sum([x for x in args if x < 0])
    positive_sum = sum([x for x in args if x > 0])
    
    return negative_sum, positive_sum

negative, positive = negative_positive(
    *[int(x) for x in input().split()]
)

print(negative)
print(positive)

if abs(negative) > positive:
    print('The negatives are stronger than the positives')
elif abs(positive) > negative:
    print('The positives are stronger than the negatives')