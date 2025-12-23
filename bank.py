class Bank :
    def __init__(self, account, balance=0):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass
    def get_balance(self):
        return self.balance