class Bank :
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" ฝากเงิน {amount} สำเร็จ ยอดคงเหลือ :{self.balance}")
        else :
            print(" ยอดคงเหลือต้องมากกว่า 0 ")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f" ยอดถอน {amount} สำเร็จ ยอดคงเหลือ :{self.balance}")
        else :
            print("ยอดเงินไม่เพียงพอ")

    def get_balance(self):
        return self.balance
    
Bank_system = Bank("โชกุน", 1000)
Bank_system.deposit(1000)
Bank_system.withdraw(1000)