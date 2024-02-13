from money import Money
import unittest
from money import Bank
from expression import Expression
from money import Sum

class Test_Money(unittest.TestCase):

    def test_equals(self):
        dollar_1 = Money.dollar(2)
        dollar_2 = Money.dollar(2)
        different_dollar = Money.dollar(10)

        result = dollar_1.__eq__(dollar_2)

        self.assertTrue(result)
        self.assertNotEqual(dollar_1, different_dollar)
        self.assertTrue(Money.dollar(5).__eq__(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).__eq__(Money.dollar(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))
        self.assertTrue(Money(10, "CHF").__eq__(Money.franc(10))) 

    def test_dollar_times(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10)._amount, five.times(2)._amount)
        self.assertEqual(Money.dollar(15)._amount, five.times(3)._amount)


    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1)._currency)
        self.assertNotEqual("CHF", Money.dollar(1)._currency)


    def test_simple_addition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank:Bank = Bank()
        
        reduced:Money = bank.reduce(sum, "USD")

        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five: Money = Money.dollar(5)
        result: Expression = five.plus(five)

        sum: Sum = result

        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def test_reduce_sum(self):
        sum: Expression = Sum(Money.dollar(3), Money.dollar(4))
        bank: Bank = Bank()

        result: Money = bank.reduce(sum, "USD")
        print(Money.dollar(7)._amount)
        print(Money.dollar(7)._currency)
        print(result._amount)
        print(result._currency)
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self): 
        bank = Bank()

        result: Money = bank.reduce(Money.dollar(1), "USD")
        
        self.assertEqual(Money.dollar(1), result)
        




    


        