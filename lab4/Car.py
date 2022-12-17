import decimal

from Driver import Driver
from Engine import Engine


class Car:
    model: str
    driver: Driver
    engine: Engine
    type: str
    weight: decimal.Decimal

    def __init__(self, model: str, driver: Driver, engine: Engine, type: str, weight):
        self.model = model
        self.driver = driver
        self.engine = engine
        self.type = type
        self.weight = weight

    @staticmethod
    def start():
        print("Car started driving!")

    @staticmethod
    def stop():
        print('Car stopped!')

    @staticmethod
    def turn_right():
        print('Car turning to right!')

    @staticmethod
    def turn_left():
        print('Car turning to left!')

    def __str__(self):
        return f'{self.model=}, {self.type=}, {self.driver.__str__()=}, ' \
               f'{self.engine.__str__()=}, {self.weight=}'
