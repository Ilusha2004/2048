import random
import pygame
from Pallete import chooseColor

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

    # def DrawField(self, field, screen, font):
    #     PosX : int = 0
    #     PosY : int = 0

    #     for line in field.getField():
    #         for item in line:
    #             pygame.draw.rect(screen, chooseColor(item).value,
    #                             (125 * PosX + 5, 125 * PosY + 5, 120, 120),
    #                             0, 20)

    #             if item != 0 and PosY == 0 and PosX == 0:
    #                 screen.blit(font.render(str(item), True,
    #                                         (255, 255, 255)),
    #                             (135 * PosX + 20, 135 * PosY + 5))

    #             elif item != 0:
    #                 screen.blit(font.render(str(item), True,
    #                                         (255, 255, 255)),
    #                             (135 * PosX + 20, 135 * PosY + 5))

    #             PosX += 1
    #         PosY += 1
    #         PosX = 0

    def getField(self):
        return self.field

    def setField(self, new_field) -> None:
        self.field = new_field
