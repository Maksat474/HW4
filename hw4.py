class SavingAccount:
    pass


class CheckingAccount:
    pass


class RealEstate:
    pass


class Stock:
    pass


class Bond:
    pass


class BankAccount(SavingAccount, CheckingAccount):
    pass


class Security(Stock, Bond):
    pass


class InterestBearingItem(BankAccount, Security):
    pass


class Asset(BankAccount, Security, RealEstate):
    pass


class InsurableItem(BankAccount, RealEstate):
    pass
