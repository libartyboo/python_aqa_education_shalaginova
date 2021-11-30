class CreditCard(object):
    def __init__(self, number, holder, status="active"):
        self.number = number
        self.holder = holder
        self.status = status

    def __str__(self):
        return f"Card: {'*' * 14 + self.number[-2:]}, Holder: {self.holder}, is {self.status}"

    def __repr__(self):
        return f"Card (last 2 numbers): {self.number[-2:]}"


credit_card = CreditCard('4000005556667779', 'John Doe')
print(credit_card)
print(repr(credit_card))