import pygame
from pygame.locals import *
from pygamepad.gamepads import Gamepad
from Field import Field
from logic import Turning, Movement
from Pallete import chooseColor

#initializing all add-ons
pygame.init()
pygame.joystick.init()
joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

screen = pygame.display.set_mode([505, 505])
field = Field(4, 4)
field.generate()
status = Turning(field.getField())
field.Draw()
status.Status()
move = Movement(field.getField())

keys = pygame.key.get_pressed()
font = pygame.font.SysFont('Arial', 60)

running = True
prev_field : list = list()

while running:

    for event in pygame.event.get():

        #keyboard input
        if keys[pygame.K_UP]:
            temp = move.move_up(field.getField())[0]
            field.setField(temp)
            field.add()
            field.Draw()

        elif keys[pygame.K_DOWN]:
            temp = move.move_down(field.getField())[0]
            field.setField(temp)
            field.add()
            field.Draw()

        elif keys[pygame.K_RIGHT]:
            temp = move.move_right(field.getField())[0]
            field.setField(temp)
            field.add()
            field.Draw()

        elif keys[pygame.K_LEFT]:
            temp = move.move_left(field.getField())[0]
            field.setField(temp)
            field.add()
            field.Draw()

        #gamepad input
        if event.type == JOYBUTTONUP:
            if event.dict.get('button') == 11:
                temp = move.move_up(field.getField())[0]
                field.setField(temp)
                field.add()
                field.Draw()

            elif event.dict.get('button') == 12:
                temp = move.move_down(field.getField())[0]
                field.setField(temp)
                field.add()
                field.Draw()

            elif event.dict.get('button') == 13:
                temp = move.move_left(field.getField())[0]
                field.setField(temp)
                field.add()
                field.Draw()

            elif event.dict.get('button') == 14:
                temp = move.move_right(field.getField())[0]
                field.setField(temp)
                field.add()
                field.Draw()


        if event.type == pygame.QUIT:
            running = False

    screen.fill((186, 173, 160))

    PosX : int = 0
    PosY : int = 0

    for line in field.getField():
        for item in line:
            pygame.draw.rect(screen, chooseColor(item).value,
                            (125 * PosX + 5, 125 * PosY + 5, 120, 120),
                            0, 20)

            if item != 0 and PosY == 0 and PosX == 0:
                screen.blit(font.render(str(item), True,
                                        (255, 255, 255)),
                            (135 * PosX + 20, 135 * PosY + 5))

            elif item != 0:
                screen.blit(font.render(str(item), True,
                                        (255, 255, 255)),
                            (135 * PosX + 20, 135 * PosY + 5))

            PosX += 1
        PosY += 1
        PosX = 0

    pygame.display.flip()

pygame.quit()