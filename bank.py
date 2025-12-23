class Bank :
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"ฝากเงิน {amount} สำเร็จ! ยอดคงเหลือ: {self.balance}")
        else:
            print("ยอดเงินฝากต้องมากกว่า 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"ถอนเงิน {amount} สำเร็จ! ยอดคงเหลือ: {self.balance}")
        else:
            print("ยอดเงินไม่เพียงพอ ")

Bank_system = Bank("Natthawut", 1000)
Bank_system.deposit(1000)