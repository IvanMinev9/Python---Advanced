def even_odd_filter(**kwargs):
    result = {}
    for key, values in kwargs.items():
        if key == "even":
            result[key] = [x for x in values if x % 2 == 0]
        elif key == "odd":
            result[key] = [x for x in values if x % 2 != 0]
    
    
    return dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))
    
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

#-------------
def even_odd_filter(*args):
    *numbers, command = args
    
    if command == "even":
        return list(filter(lambda x: x % 2 == 0))
    return list(filter(lambda x: x % 2 != 0))
