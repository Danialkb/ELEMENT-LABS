import sys

from handler import UserHandler
from repository import AccountRepo
from bank_account import BankAccount
from currency import Currency


def init():
    user_repos = AccountRepo()
    user_handler = UserHandler(user_repos)
    # print(type(Currency.KZT.name))
    while True:
        c1 = input('1.To sign up enter "sign up".\n'
                   '2.To sign in enter "sign in"\n'
                   '3.To exit enter "q"\n').strip()
        if c1 == 'q':
            sys.exit(0)
        elif c1 == 'sign up':
            name, surname, password = input('Enter name, surname and password: ').split()
            user_handler.sign_up(name=name, surname=surname, password=password)
        elif c1 == 'sign in':
            name, surname, password = input('Enter name, surname and password: ').split()
            cur_acc = user_handler.sign_in(name=name, surname=surname, password=password)
            if cur_acc is not None:
                while True:
                    c2 = int(input('1.To add to account enter "1".\n'
                                   '2.To substract from account enter "2"\n'
                                   '3.To convert money enter "3"\n'
                                   '4.To exit enter "4"\n'))
                    if c2 == 1:
                        value = float(input('Enter value\n'))
                        cur_acc.add_to_acc(value)
                    elif c2 == 2:
                        value = float(input('Enter value\n'))
                        cur_acc.substract_from_acc(value)
                    elif c2 == 3:
                        currency = input('Enter currency: KZT, USD, EUR, RUB\n').strip()
                        if currency == 'KZT':
                            cur_acc.money_conversion(Currency.KZT)
                        elif currency == 'RUB':
                            cur_acc.money_conversion(Currency.RUB)
                        elif currency == 'USD':
                            cur_acc.money_conversion(Currency.USD)
                        elif currency == 'EUR':
                            cur_acc.money_conversion(Currency.EUR)
                    elif c2 == 4:
                        break
                    else:
                        print('Invalid command!')

        else:
            print('Invalid command!')


if __name__ == '__main__':
    init()
