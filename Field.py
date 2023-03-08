import random

class Field:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self) -> None:

        bar : int = 0

        self.field : list = [[bar for _ in range(4)] for _ in range(4)]

        for _ in range(2):
            self.add()

    def add(self):

        x = random.randint(0, 3)
        y = random.randint(0, 3)

        while(self.field[x][y] != 0):
            x = random.randint(0, 3)
            y = random.randint(0, 3)

        number = random.choice([2, 4])
        bar = number
        self.field[x][y] = bar

    def Update(self, field : list):
        self.field = field

    def Draw(self):
        for line in self.field:
            for b in line:
                print(b, end = ' ')
            print()

    def getField(self):
        return self.field

    def setField(self, new_field) -> None:
        self.field = new_field
