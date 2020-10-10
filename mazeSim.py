import pygame

#Color Const
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Robot(): #pygame.sprite.Sprite
 
    xSpeed = 0
    ySpeed = 0
 
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the robot. Called with a keypress. """
        self.xSpeed += x
        self.ySpeed += y
 
    def move(self, walls):
        # Move left/right
        self.rect.x += self.xSpeed
 
        # Collision check
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.xSpeed > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.ySpeed
 
        # Collision check
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.ySpeed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


length = 80
xOffset = 80
walls = []
walls.append([(xOffset + 0,0),(xOffset + 480,0)])
walls.append([(xOffset + 480,0),(xOffset + 480,80)])
walls.append([(xOffset + 480,160),(xOffset + 480,480)])
walls.append([(xOffset + 480,480),(xOffset + 0,480)])
walls.append([(xOffset + 0,480),(xOffset + 0,160)])
walls.append([(xOffset + 0,80),(xOffset + 0,0)])
walls.append([(xOffset + 0,160),(xOffset + 80,160)])
walls.append([(xOffset + 80,80),(xOffset + 80,160)])
walls.append([(xOffset + 80,240),(xOffset + 80,480)])
walls.append([(xOffset + 160,0),(xOffset + 160,400)])
walls.append([(xOffset + 240,80),(xOffset + 240,400)])
walls.append([(xOffset + 240,400),(xOffset + 400,400)])
walls.append([(xOffset + 400,400),(xOffset + 400,480)])
walls.append([(xOffset + 320,0),(xOffset + 320,240)])
walls.append([(xOffset + 320,320),(xOffset + 320,400)])
walls.append([(xOffset + 400,80),(xOffset + 400,320)])


def main():

    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Maze Simulation')

        # Create the robot paddle object
    robot = Robot(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(robot)

    clock = pygame.time.Clock()
 
    done = False

    while not done:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        robot.move(current_room.wall_list)
 
        if robot.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                robot.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                robot.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 790
 
        if robot.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                robot.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                robot.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 0
 
        # --- Drawing ---
        screen.fill(BLACK)
 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()