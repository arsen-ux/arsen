class Asset:
    pass

class InterestBearingItem(Asset):
    pass

class InsurableItem(Asset):
    pass

class RealEstate(InsurableItem):
    pass

class Security(InterestBearingItem):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass

class BankAccount(Asset):
    pass

class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass