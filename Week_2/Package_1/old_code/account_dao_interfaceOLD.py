from abc import ABC, abstractmethod

from Week_2.Package_1.old_code.bank_account import BankAccount

class AccountDAOInterface(ABC):
    #
    @abstractmethod
    def create_deposit(self, account_id: BankAccount) -> BankAccount:
        pass
    #
    @abstractmethod
    def get_current_balance(self, account_id: int) -> BankAccount:
        pass
    #
    @abstractmethod
    def withdraw_amount(self, account_id: BankAccount) -> BankAccount:
        pass
    #
    @abstractmethod
    def transfer_amount(self, account_id: int) -> BankAccount:
        pass
    #
    @abstractmethod
    def delete_account(self, account_id: int) -> bool:
        pass