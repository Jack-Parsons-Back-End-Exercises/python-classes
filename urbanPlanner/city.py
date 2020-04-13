import time

class City:

    def __init__(self, name, mayor):
        self.name = name
        self.mayor = mayor
        self.year_estabilished =  time.localtime()
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def generate_city_report(self):
        print("BUILDING REPORT")
        print("")
        print("***********************************")
        for building in self.buildings:
            print("")
            print(f'Address: {building.address}')
            print(f'Stories: {building.stories}')
            print(f'Year Constructed: {building.date_constructed.tm_year}')
            print(f'Owner: {building.owner}')
            print(f'Designer: {building.designer}')
            print("")
            print("***********************************")
