class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        return f"le solde de {self.owner}: {self.balance} FCFA"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depot effectuer: {amount} FCFA"
        else:
            return f"Montant invalide"



account = BankAccount("Alice", 1000)
print(account.show_balance())
print(account.deposit(500))
print(account.show_balance())
print(account.deposit(-100))
print(account.show_balance())

