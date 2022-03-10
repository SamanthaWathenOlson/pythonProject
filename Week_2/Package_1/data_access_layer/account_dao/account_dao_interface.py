from abc import ABC, abstractmethod

from objects.account_class_info import Account
from objects.bank_class_info import Bank


class AccountDAOInterface(ABC):

    # create
    @abstractmethod
    def create_account_id(self, account_id, customer_id, account: Account) -> Account:
        pass

    # read
    @abstractmethod
    def get_account_id(self, account_id: int, customer_id, account: Account) -> Account:
        pass

    @abstractmethod
    def find_all_accounts(self, customer_id, account_id, balance_from, bank: Bank) -> Bank:
        pass

    # update
    @abstractmethod
    def update_account(self, account_id, customer_id, first_name, last_name, account: Account) -> Account:
        pass

    # delete
    @abstractmethod
    def delete_account_id(self, balance, customer_id, account_id: int) -> bool:
        pass

    @abstractmethod
    def get_account_balance(self, account_id, customer_id, balance, account: Account) -> Account:
        pass

    @abstractmethod
    def deposit_to_account(self, account_to,deposit_to, balance_from, bank:Bank) -> Bank:
        pass

    @abstractmethod
    def transfer_my_balance(self, to_account, balance_from, transfer_from, bank: Bank) -> Bank
        pass

    @abstractmethod
    def transfer_amount(self, to_account, deposit_to, balance_from, bank: Bank) -> Bank:
        pass

    def withdraw_from_balance(self, to_account, from_account, withdraw_from, balance_from, bank: Bank) -> Bank:
        pass
