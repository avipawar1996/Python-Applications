'''
Write a python program to implement a class named BankAccount with the following requirements:
    - Class should contain two instance variable:
        Name(Account Holder Name) and Amount (Account Balance)
    - Class should contain one class variable:
        ROI (Rate of Interest), initialized to 10.5
    - Define a constructor (__init__()) that accept Name and initial amount.
    - Implement an instance methods:
        Display() - display account holder name and current balance
        Deposit() - accept an amount from user and adds it to balance
        Withdraw() - accept an amount from user and substract it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
        CalculateInterest() - calculate and returns interest using formula:
            Interest = (Amount * ROI) / 100
    - Create multiple objects and demonstrate all methods.
'''

class BankAccount:

    ROI: float = 10.5

    def __init__(self, acc_holder_name:str, acc_balance: float):
        self.acc_holder_name = acc_holder_name
        self.acc_balance = acc_balance

    def Display(self):
        print(f"\n Account Holder Name: {self.acc_holder_name}\n Account Balance: {self.acc_balance}")

    def Deposit(self, deposit_amt): self.acc_balance = self.acc_balance + deposit_amt
    def Withdraw(self, withdraw_amt):
        if(self.acc_balance - withdraw_amt >= 0):
            self.acc_balance = self.acc_balance - withdraw_amt
            print(f"\n Withdrawal Amount: {withdraw_amt} successful. Current Balance: {self.acc_balance}")
        else:
            print(f"\n Withdrawal Amount: {withdraw_amt}: Insufficient amount to withdraw.")
    def CalculateInterest(self): return (self.acc_balance * BankAccount.ROI) / 100


Obj1 = BankAccount("John Richard", 500)
Obj1.Display()

Obj1.Deposit(float(input(" Enter deposit amount: ")))

print(f" Calculated Interest Amount: {Obj1.CalculateInterest()}")

Obj1.Withdraw(float(input(" Enter amount to withdraw: ")))
Obj1.Display()
print(" -------------------------------------------------")

Obj2 = BankAccount("Rickulton Philips", 800)
Obj2.Display()

Obj2.Deposit(float(input(" Enter deposit amount: ")))

print(f" Calculated Interest Amount: {Obj2.CalculateInterest()}")

Obj2.Withdraw(float(input(" Enter amount to withdraw: ")))
Obj2.Display()
print(" -------------------------------------------------")

Obj3 = BankAccount("Bob Biden", 1000)
Obj3.Display()

Obj3.Deposit(float(input(" Enter deposit amount: ")))

print(f" Calculated Interest Amount: {Obj3.CalculateInterest()}")

Obj3.Withdraw(float(input(" Enter amount to withdraw: ")))
Obj3.Display()
print(" -------------------------------------------------")