from customer_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_dao.customer_dao_interface import AccountDAOInterface
from objects.customer_information import BankAccount

AccountDAOInterface

class AccountDAOImp(AccountDAOInterface):

account_list [1]
id_generator =2

def __int__(self):
    account_needed_for_id_catch = BankAccount(1, "234789")
    self.account_list.append(account_needed_for_id_catch)

def create_account(self, account:  BankAccount)-> BankAccount:
    account.account_id = self.id_generator
    self.id_generator += 1
    self.account_list.append(account)
    return account
#
def get_account_information_by_id(self, account_id: int) -> BankAccount:
    for account in self.account_list:
        if account.account_id == account_id:
            return account_id
    raise IdNotFound("No customer matches the id given. Please try again.")
#
def get_all_accounts_for_user(self, account_id: int, customer_id: int) -> BankAccount:
    for account_id in self.account_list:
        if accoun.account_id == account_id
            return account_id
    raise IdNotFound("No customer matches the id given. Please try again")

def delete_account_by_id(self,  account_id: int)-> bool:
    for account in self.account_list:
        if account.account_id == account_id:
            self.account_list.remove(account)
            return True
    raise IdNotFound("No customer matches the id given. Please try again")


