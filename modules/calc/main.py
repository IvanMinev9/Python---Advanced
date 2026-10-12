from core import calc_operation

expre = input().split()
num1 = float(expre[0]) 
num2 = float(expre[2]) 
sign = expre[1] 
print(f"{calc_operation(num1, num2, sign):.2f}")