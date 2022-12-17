import decimal


class Engine:
    power: decimal.Decimal
    producer: str

    def __init__(self, power, producer):
        self.power = power
        self.producer = producer

    def __str__(self):
        return f'{self.power=}, {self.producer=}'
