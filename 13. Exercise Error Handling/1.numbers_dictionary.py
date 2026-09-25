numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError as err:
        print(f"The variable number must be an integer - More information => {err}")
    else:
        numbers_dictionary[number_as_string] = number
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError as err:
        print(f"Number does not exist in dictionary - More information => {err}")
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError as err:
        print(f"Number does not exist in dictionary - More information => {err}")
    line = input()

print(numbers_dictionary)
