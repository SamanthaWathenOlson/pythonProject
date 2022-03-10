from abc import ABC, abstractmethod
from objects.team_class_infromation import CustomerId

class BankServiceInterface(ABC):

    @abstractmethod
    def service_balance(self, value, account_id):
        pass

    @abstractmethod
    def service_deposit(self, value, account_id):
       pass

    @abstractmethod
    def service_withdraw(self, value, account_id):
        pass

    @abstractmethod
    def service_transfer(self, value, account_id):
        pass

    @abstractmethod
    def service_transfer_full_amount(self, value, account_id):
        pass