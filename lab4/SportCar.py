import decimal

from Car import Car
from Engine import Engine
from Driver import Driver


class SportCar(Car):
    speed: decimal.Decimal

    def __init__(self, model: str, driver: Driver, engine: Engine, type: str, weight, speed: decimal.Decimal):
        super().__init__(model, driver, engine, type, weight)
        self.speed = speed

    def __str__(self):
        return super().__str__() + f', {self.speed=}'
