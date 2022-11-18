class Account:
    def __init__(self, name: str) -> None:
        '''
        Constructor to create different account objects.
        :param name: Person's first name.
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Method to deposit money into account's balance.
        :param amount: The amount of money to deposit.
        :return: True, if the action was successful. False, if the action did nothing.
        '''
        if amount == 0:
            return False
        elif amount < 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        Method to withdraw money out of account's balance.
        :param amount: The amount of money to withdraw.
        :return: True, if the action was successful. False, if the action did nothing.
        '''
        if amount == 0:
            return False
        elif amount < 0:
            return False
        elif amount > self.get_balance():
            return False
        else:
            self.__account_balance -= amount

    def get_balance(self) -> float:
        '''
        Method to get access to account's balance.
        :return: amount of money inside of balance.
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to get access to the person's first name of the account.
        :return: The person's first name.
        '''
        return self.__account_name


