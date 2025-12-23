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

class SavingsAccount(Bank):
    def __init__(self, account, balance=0, interesr = 0.02):
        super().__init__(account, balance)
        self.interesr = interesr
    def apply_interesr(self):
        interesr = self.balance * self.interesr
        self.balance += interesr
        print(f"คำนวณดอกเบี้ยเรียบร้อย! ได้รับ: {interesr} | ยอดเงินรวมใหม่: {self.balance}")

Savings = SavingsAccount("Natthawut",1000)
Savings.apply_interesr()

import datetime

class BankSecurity:
    @staticmethod
    def validate_amount(amount):
        """ตรวจสอบว่าตัวเลขถูกต้อง (มากกว่า 0 และเป็นตัวเลข)"""
        if isinstance(amount, (int, float)) and amount > 0:
            return True
        print(" Error: จำนวนเงินต้องเป็นตัวเลขที่มากกว่า 0")
        return False

    @staticmethod
    def log_transaction(action, holder, amount):
        """บันทึกประวัติการทำรายการพร้อมเวลา"""
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"LOG - {now}] บัญชี {holder}: {action} จำนวน {amount}")

# --- ส่วนการทดสอบโดย Member 3 ---

# 1. สร้างบัญชีทดสอบ
my_account = SavingsAccount("Natthawut", 1000)

print("--- เริ่มการทดสอบระบบ Security ---")

# 2. ทดสอบฝากเงินด้วยจำนวนที่ถูกต้อง
test_amount = 500
if BankSecurity.validate_amount(test_amount):
    my_account.deposit(test_amount)
    BankSecurity.log_transaction("Deposit", my_account.account, test_amount)
    

# 3. ทดสอบถอนเงินด้วยจำนวนที่ "ผิดกฎ" (เช่น ติดลบ)
bad_amount = -100
print(f"\nกำลังทดสอบถอนเงินจำนวน: {bad_amount}")
if BankSecurity.validate_amount(bad_amount):
    my_account.withdraw(bad_amount)
else:
    print("ระบบ Security ดักจับยอดเงินติดลบได้ถูกต้อง!")

# 4. ทดสอบถอนเงินเกินยอดคงเหลือ
over_amount = 5000
print(f"\nกำลังทดสอบถอนเงินจำนวน: {over_amount}")
if BankSecurity.validate_amount(over_amount):
    my_account.withdraw(over_amount)

