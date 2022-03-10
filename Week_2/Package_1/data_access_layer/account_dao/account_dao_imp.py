from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.account_dao.account_dao_interface import AccountDAOInterface
from objects.account_class_info import Account


class AccountDAOImp(AccountDAOInterface):

    def __init__(self):
        account_needed_for_id_catch = Account(1, 32867495, 34569847, 500.00)
        self.account_list = []
        self.id_generator = 2

        self.account_list.append(account_needed_for_id_catch)

    # create
    def create_account(self, account: Account) -> Account:
        account.account_id = self.id_generator
        self.id_generator += 1
        self.account_list.append(account_id)
        return account

    # read
    def get_account_information_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account_id
        raise IdNotFound("No account matches the id given: please try again!")

    # update
    def update_account_by_id(self, account, Account) -> Account:
        for previous_account in self.account_list:
            if previous_account.account_id == account.account_id:
                previous_account = account
                return previous_account
        raise IdNotFound("No account matches the id given: please try again!")

    # delete
    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
            return True
    raise IdNotFound("No account matches the id given: please try again!")