from functools import reduce

def sum_num(*args):
    return sum(args)

def sub(*args):
    return reduce(lambda x, y: x - y, args)

def mult(*args):
    return reduce(lambda x, y: x * y, args)

def dev(*args):
    return reduce(lambda x, y: x / y, args)    
    

mapper = {
    "+": sum_num,
    "-": sub,
    "*": mult,
    "/": dev
}    
def operate(char, *args):
    func = mapper[char]
    return func(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
