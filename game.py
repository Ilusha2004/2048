import pygame
from Field import Field
from logic import Turning, Movement

pygame.init()

screen = pygame.display.set_mode([500, 500])
field = Field(4, 4)
field.generate()
status = Turning(field.getField())
field.Draw()
status.Status()
move = Movement(field.getField())

keys = pygame.key.get_pressed()
font = pygame.font.SysFont('Arial', 60)

running = True

while running:

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

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

        if event.type == pygame.QUIT:
            running = False

    screen.fill((192, 192, 192))

    x : int = 0
    y : int = 0

    for line in field.getField():
        for item in line:
            pygame.draw.rect(screen, (50 * (x + 1), 50 * (x + 1), 0),
                             (125 * x, 125 * y, 125, 125),
                             0, 20)

            if item != 0 and y == 0 and x == 0:
                screen.blit(font.render(str(item), True, (255, 255, 255)), (135 * x + 20, 135 * y + 5))

            elif item != 0:
                screen.blit(font.render(str(item), True, (255, 255, 255)), (135 * x + 20, 135 * y + 5))

            # elif item != 0 and y == 3 and
            x += 1
        y += 1
        x = 0

    pygame.display.flip()

pygame.quit()