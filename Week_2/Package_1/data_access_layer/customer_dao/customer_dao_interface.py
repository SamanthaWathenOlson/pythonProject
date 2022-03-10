from abc import ABC, abstractmethod

from objects.customer_class_info import Customer


class CustomerDAOInterface(ABC):

    # Create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # Read
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # Update
    @abstractmethod
    def update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    # Delete
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
