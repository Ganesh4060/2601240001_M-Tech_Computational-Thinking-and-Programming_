from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BankAccount(ABC):
    account_number: str
    customer_name: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def display(self) -> None:
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)


@dataclass
class SavingsAccount(BankAccount):

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Savings withdrawal successful")


@dataclass
class CurrentAccount(BankAccount):

    overdraft_limit: float = 1000.0

    def withdraw(self, amount: float) -> None:
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            print("Current account withdrawal successful")


# Main

savings = SavingsAccount(
    account_number="S101",
    customer_name="Ganesh",
    balance=5000
)

current = CurrentAccount(
    account_number="C101",
    customer_name="Rahul",
    balance=3000
)

savings.deposit(1000)
savings.withdraw(2000)

print("\nSavings Account")
savings.display()

current.withdraw(3500)

print("\nCurrent Account")
current.display()