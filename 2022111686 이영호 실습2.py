class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def Deposit(self, amount):
       if amount > 0:
           self.balance += amount
           print("5000원이 입금되었습니다.")
       else:
           print("0원보다 커야합니다")

    def withdraw(self, amount):
        if amount < self.balance:
            print("돈이 부족하여 출금할 수 없습니다.")
        else:
            print("0원보다 커야합니다")

    def display_balance(self):
        print("현재잔액: 999,999,999원")

account = BankAccount("이영호", 10000)

account.Deposit(5000)

account.withdraw(10)
account.display_balance()




