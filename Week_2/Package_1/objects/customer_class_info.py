class Customer:

    def __init__(self, customer_id: int, account_id: int, customer_name: str, first_name: str, last_name: str, address: str):
        self.customer_id = customer_id
        self.account_id = account_id
        self.customer_name = customer_name
        self.first_name = first_name
        self.last_name = last_name
        self.address = address