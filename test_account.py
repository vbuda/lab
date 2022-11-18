from account import *
import unittest

class account_testing(unittest.TestCase):
    def setUp(self) -> None:
        self.account1 = Account('jane')
        self.account2 = Account('jill')

    def tearDown(self) -> None:
        del self.account1
        del self.account2

    def test_init(self):
        self.assertEqual(self.account1.get_name(), 'jane')
        self.assertEqual(self.account1.get_balance(), 0)
        self.assertEqual(self.account2.get_name(), 'jill')
        self.assertEqual(self.account2.get_balance(), 0)

    def test_deposit(self):
        self.account1.deposit(10)
        self.assertEqual(self.account1.get_balance(), 10)
        self.account1.deposit(5)
        self.assertEqual(self.account1.get_balance(), 15)
        self.account2.deposit(0)
        self.assertEqual(self.account2.get_balance(), 0)
        self.account1.deposit(-1)
        self.assertEqual(self.account1.get_balance(), 15)

    def test_withdraw(self):
        self.account1.withdraw(-100)
        self.assertEqual(self.account1.get_balance(), 0)
        self.account2.deposit(10)
        self.account2.withdraw(1)
        self.assertEqual(self.account2.get_balance(), 9)
        self.account2.withdraw(10)
        self.assertEqual(self.account2.get_balance(), 9)




