"""Functions for calculating steps in exchanging currency.
Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget/exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount//denomination


def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount - amount//denomination * denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
"""
    actual_rate = exchange_rate * (1 + spread / 100)
    exchanged_amount = exchange_money(budget, actual_rate)
    num_bills = get_number_of_bills(exchanged_amount, denomination)

    return num_bills * denomination


test_data = [(100000, 10.61, 10, 1),
             (1500, 0.84, 25, 40),
             (470000, 1050, 30, 10000000000),
             (470000, 0.00000009, 30, 700),
             (425.33, 0.0009, 30, 700)]

result_data = [8568, 1400, 0, 4017094016600, 363300]

# print(exchangeable_value(127.25, 1.20, 10, 20))  # Should output 80
# print(exchangeable_value(127.25, 1.20, 10, 5))   # Should output 95

for idx, test in enumerate(test_data):
    assert exchangeable_value(*test)==result_data[idx]

