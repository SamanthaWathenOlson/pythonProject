from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from objects.customer_class_info import Customer


class CustomerDAOImp(CustomerDAOInterface):

    customer_list = [Customer(1, 1, "Samantha", "Wathen", "Indianapolis,In")]
    id_generator = 2

    # Create
    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.id_generator
        self.id_generator += 1
        self.customer_list.append(customer)
        return customer

    # Read
    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                return customer
        raise IdNotFound("No customer matches the id given: please try again!")

    # Update
    def update_customer_by_id(self, customer: Customer) -> Customer:
        for previous_customer in self.customer_list:
            if previous_customer.customer_id == customer.customer_id:
                previous_customer = customer
                return previous_customer
        raise IdNotFound("No customer matches the id given: please try again!")

    # Delete
    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customer_list:
            if customer.customer_id== customer_id:
                self.customer_list.remove(customer)
                return True
        raise IdNotFound("No customer matches the id given: please try again!")