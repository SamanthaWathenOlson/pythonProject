class Bank:

    def __init__(self, to_account, from_account, deposit_to, withdraw_from, transfer_from, balance_from):
        self.to_account = to_account(float)
        self.from_account = from_account(float)
        self.deposit_to = deposit_to(float)
        self.withdraw_from = withdraw_from(float)
        self.transfer_from = transfer_from(float)
        self.balance_from = balance_from(float)
