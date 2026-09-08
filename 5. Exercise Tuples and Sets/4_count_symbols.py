text = input()
symbols = set()

for char in text:
    symbols.add(char)

for char in sorted(symbols):
    print(f'{char}: {text.count(char)} time/s')