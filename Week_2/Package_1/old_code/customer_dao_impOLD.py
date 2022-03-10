from customer_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from objects.customer_information import CustomerId

CustomerDAOInterface

class CustomerDAOImp(CustomerDAOInterface):

customer_list [1]
id_generator =2

def __int__(self):
    customer_needed_for_id_catch = CustomerId(1, "Samantha" , "Wathen")
    self.customer_list.append(customer_needed_for_id_catch)

def create_customer(self, customer:  CustomerId)-> CustomerId:
    customer.customer_id = self.id_generator
    self.id_generator += 1
    self.customer_list.append(customer)
    return customer

def get_customer_information_by_id(self, customer_id: int) ->CustomerId:
    for customer in self.customer_list:
        if customer.customer_id == customer_id:
            return customer_id
    raise IdNotFound("No customer matches the id given. Please try again.")

#def get_all_accounts_for_user(self, customer_id: int, account_id: int) ->CustomerId:
#    for customer_id in self.account_list:
#        if customer.account_id == customer_id
#            return customer_id
#    raise IdNotFound("No customer matches the id given. Please try again")

def update_customer_by_id(self, customer: CustomerId)->CustomerId:
    for previous_customer_id in self.customer_list:
        if customer.customer_id == previous_customer_id.customer_id:
            previous_customer_id = customer
            return previous_customer_id
    raise IdNotFound("No customer matches the id given. Please try again")

def delete_customer_by_id(self,  customer_id: int)-> bool:
    for customer in self.customer_list:
        if customer.customer_id == customer_id:
            self.customer_list.remove(customer)
            return True
    raise IdNotFound("No customer matches the id given. Please try again")


