"""_summary_

Raises:
	AttributeError: _description_
	AttributeError: _description_
"""

import  sys
from    typing  import  List

class Account(object):
    """_summary_

    Args:
        object (_type_): _description_

    Raises:
        AttributeError: _description_
        AttributeError: _description_
    """

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        """_summary_

        Args:
            name (_type_): _description_

        Raises:
            AttributeError: _description_
            AttributeError: _description_
        """
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def	transfer(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        self.value += amount

class Bank(object):

    """_summary_
    """

    def __init__(self):
        self.accounts: List[Account] = []

    def add(self, new_account: Account=None):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
                    @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # # it can be appended to the attribute accounts
        # ... Your code ...
        if not isinstance(new_account, Account):
            return False
        for account in self.accounts:
            if new_account.name is account.name:
                return False
        self.accounts.append(new_account)
        return True

    def check_account(self, account: Account):
        """_summary_

        Args:
            account (Account): _description_

        Returns:
            _type_: _description_
        """
        naddr = 0
        nzip = 0
        for attr in account.__dict__.keys():
            if attr.startswith("b"):
                return(False)
            if attr.startswith("addr"):
                naddr += 1
            if attr.startswith("zip"):
                nzip += 1
        if len(account.__dict__) % 2 == 0 \
                or naddr == 0 \
                or nzip == 0 \
                or account.__dict__.get("name") is False \
                or account.__dict__.get("id") is False \
                or account.__dict__.get("value") is False \
                or isinstance(account.__dict__.get("name"), str) is False \
                or isinstance(account.__dict__.get("id"), int) is False \
                or (isinstance(account.__dict__.get("value"), (float, int)) is False):
            return False
        return True

    def transfer(self, origin: Account, dest, amount) -> bool:
        """ Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if amount < 0:
            print("Error: Not a valid amount.")
            return False
        account1 = account2 = None
        for account in self.accounts:
            if account.name is origin:
                account1 = account
            if account.name is dest:
                account2 = account
        if (account1 is None or account2 is None):
            print("Error: Origin or Des are not registered in this bank.")
            return False
        if not self.check_account(account1):
            print("Error: Corrupted account origin")
            return False
        if not self.check_account(account2):
            print("Error: Corrupted account2 dest")
            return False
        if account1.value < amount:
            print("Error: Not enough money in account origin")
            return False
        if account1.name is account2.name:
            return True
        account1.value -= amount
        account2.value += amount
        return True

        # ... Your code ...

    def fix_account(self, name):
        """ fix account associated to name if corrupted
                    @name:   str(name) of the account
                    @return  True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account1 = None
        for account in self.accounts:
            if name is account.name:
                account1 = account
                break
        if (account1 is None):
            return False
        naddr = 0
        nzip = 0
        for attr in dir(account1.__dict__):
            if attr.startswith("b") is True:
                account1.__dict__.pop(attr)
            if attr.startswith("zip"):
                nzip += 1
            if attr.startswith("addr"):
                naddr += 1
        if "name" in dir(account1.__dict__) and not isinstance(account1.__dict__.get("name"), str):
            account1.__dict__.pop("name")
        if "id" in dir(account1.__dict__) and not isinstance(account1.__dict__.get("id"), int):
            account1.__dict__.pop("name")
        if "value" in dir(account1.__dict__) and not isinstance(account1.__dict__.get('value'), (float, int)):
            account1.__dict__.pop("name")
        if "name" not in dir(account1.__dict__):
            account1.__dict__.update({"name": account1.name})
        if "id" not in dir(account1.__dict__):
            account1.__dict__.update({"id": account1.id})
        if "value" not in dir(account1.__dict__):
            account1.__dict__.update({"value": account1.value})
        if nzip == 0:
            account1.__dict__.update({"zip":None})
        if naddr == 0:
            account1.__dict__.update({"addr":None})
        if len((account1.__dict__)) % 2 == 0:
            account1.__dict__.update({"anything":None})
        return True
        # ... Your code ...
