from Car import Car
from Engine import Engine
from Driver import Driver


class Lorry(Car):
    carrying: int

    def __init__(self, model: str, driver: Driver, engine: Engine, type: str, weight, carrying: int):
        super().__init__(model, driver, engine, type, weight)
        self.carrying = carrying

    def __str__(self):
        return super().__str__() + f', {self.carrying=}'
