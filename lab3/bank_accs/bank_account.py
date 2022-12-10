from currency import Currency

exchange_rate = {
    ('KZT', 'USD'): 1 / 480,
    ('KZT', 'RUB'): 1 / 7,
    ('KZT', 'EUR'): 0.002,
    ('USD', 'KZT'): 480,
    ('USD', 'RUB'): 480 / 7,
    ('USD', 'EUR'): 480 / 500,
    ('RUB', 'KZT'): 7,
    ('RUB', 'EUR'): 500 / 7,
    ('RUB', 'USD'): 480 / 7,
    ('EUR', 'KZT'): 500,
    ('EUR', 'RUB'): 500 / 7,
    ('EUR', 'USD'): 500 / 480,
}


class BankAccount:
    name: str
    surname: str
    __password: str
    account: float
    currency: Currency

    def __init__(self, name: str, surname: str, password: str):
        self.name = name
        self.surname = surname
        self.__password = password
        self.account = 0
        self.currency = Currency.KZT

    def add_to_acc(self, money: float) -> None:
        self.account += money
        print(self)

    def substract_from_acc(self, money: float) -> None:
        if money > self.account:
            print('Not enough money on account!')
        else:
            self.account -= money
            print(self)

    def money_conversion(self, currency: Currency) -> None:
        for k, v in exchange_rate.items():
            if k[0] == self.currency.name and k[1] == currency.name:
                self.account *= v
                self.currency = currency
                print(self)
                return
        print('Invalid currency!!!')

    def check_password(self, password: str) -> bool:
        return self.__password == password

    def __str__(self) -> str:
        return f'{self.name=}, {self.surname=}, {self.account=}, {self.currency=}'

    def set_account(self, account: float) -> None:
        self.account = account

    def get_account(self) -> float:
        return self.account

    def __del__(self):
        print(f'Object {self} destroyed!')
