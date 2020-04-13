import time

class Building:

    def __init__(self, address, stories):
        self.designer = "Jack Parsons"
        self.date_constructed = ""
        self.owner = ""
        self.address =  address
        self.stories = stories

    def construct(self):
        self.date_constructed = time.localtime()

    def purchase(self, newOwner):
        self.owner = newOwner