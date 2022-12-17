from Car import Car
from Lorry import Lorry
from Engine import Engine
from Driver import Driver
from SportCar import SportCar
from Person import Person


d1 = Driver('dan', 19, 2)
print(d1)
c1 = Car('mers', d1, Engine(200, 'emmsms'), 'sedan', 1000)
c2 = Lorry('mers', d1, Engine(200, 'emmsms'), 'sedan', 1000, 5000)
c3 = SportCar('mers', d1, Engine(200, 'emmsms'), 'sedan', 1000, 300)
c2.start()
c3.turn_left()
print(c3)
