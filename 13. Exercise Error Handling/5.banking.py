class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

AGE_MIN = 18
pin_code, balance, age = map(int, input().split(", "))

while True:
    line = input().split("#")
    
    if line[0] == "End":
        break
    
    if line[0] == "Send Money":
        money, pin = int(line[1]), int(line[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < AGE_MIN:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        
        balance -= money
    
        print(f"Successfully sent {money} money to a friend")
        print(f"There is {balance} money left in the bank account")
    
    elif line[0] == "Receive Money":
        money = int(line[1])
        
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        amount_money = money * 0.5
        balance += amount_money
        
        print(f"{amount_money} money went straight into the bank account")