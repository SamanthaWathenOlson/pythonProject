from abc import ABC, abstractmethod

from Week_2.Package_1.old_code.customer_name import CustomerId

class CustomerDAOInterface(ABC):
    # create
    @abstractmethod
    def create_customer(self, customer_id: CustomerId) -> CustomerId:
        pass
    # read
    @abstractmethod
    def get_customer_information_by_id(self, customer_id: int) -> CustomerId:
        pass
    # update
    @abstractmethod
    def update_customer_information_by_id(self, customer_id: CustomerId) -> CustomerId:
        pass
    # delete
    @abstractmethod
    def __delete__(self, customer_id: int) -> bool:
        pass
