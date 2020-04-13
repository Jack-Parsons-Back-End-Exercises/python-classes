import time

class City:

    def __init__(self, name, mayor):
        self.name = name
        self.mayor = mayor
        self.year_estabilished =  time.localtime()
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)
