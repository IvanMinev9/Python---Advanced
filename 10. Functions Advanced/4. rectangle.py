def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    
    def area():
        return length * width
    
    def parametar():
        return 2 * length + 2 * width
    
    
    return f"Rectangle area: {area()}\n Rectangle perimeter: {parametar()}"

print(rectangle(2, 10))
print(rectangle('2', 10))
