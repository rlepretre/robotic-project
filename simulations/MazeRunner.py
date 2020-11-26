import pygame
import time
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255) 
 
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the robot controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Sensor(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Robot(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    robot controls """
 
    # Set speed vector
    xSpeed = 0
    ySpeed = 0

    junctions = []
    
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([40, 40])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.sensors = [
            Sensor(self.rect.x + 20, self.rect.y + 20, 80, 2, RED),
            Sensor(self.rect.x + 20, self.rect.y + 20, 2, 80, RED),
            Sensor(self.rect.x - 60, self.rect.y + 20, 60, 2, RED),
            Sensor(self.rect.x + 20, self.rect.y - 60, 2, 60, RED)
        ]

    def getxSpeed(self):
        return self.xSpeed
    
    def getySpeed(self):
        return self.ySpeed
 
    def changespeed(self, x, y):
        """ Change the speed of the robot. Called with a keypress. """
        self.xSpeed += x
        self.ySpeed += y
 
    def move(self, walls):
        """ Find a new position for the robot """
 
        # Move left/right
        self.rect.x += self.xSpeed
        self.sensors[0].rect.x = self.rect.x + 20
        self.sensors[1].rect.x = self.rect.x + 20
        self.sensors[2].rect.x = self.rect.x - 60
        self.sensors[3].rect.x = self.rect.x + 20
 
        # Did this update cause us to hit a wall?
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
        self.sensors[0].rect.y = self.rect.y + 20
        self.sensors[1].rect.y = self.rect.y + 20
        self.sensors[2].rect.y = self.rect.y + 20
        self.sensors[3].rect.y = self.rect.y - 60
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.ySpeed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


    def tremaux(self, walls):

        
        wallSensed = 0
        frontsensed = False
        rightsensed = False
        leftsensed = False
        backsensed = False

        frontsensor_hit_list = pygame.sprite.spritecollide(self.sensors[0], walls, False)
        for sensed in frontsensor_hit_list:
            wallSensed += 1
            frontsensed = True
        
        rightsensor_hit_list = pygame.sprite.spritecollide(self.sensors[1], walls, False)
        for sensed in rightsensor_hit_list:
            wallSensed += 1
            rightsensed = True
        
        leftsensor_hit_list = pygame.sprite.spritecollide(self.sensors[2], walls, False)
        for sensed in leftsensor_hit_list:
            wallSensed += 1
            leftsensed = True

        backsensor_hit_list = pygame.sprite.spritecollide(self.sensors[3], walls, False)
        for sensed in backsensor_hit_list:
            wallSensed += 1
            backsensed = True
            
        print(wallSensed)
        
        if(wallSensed == 1):
            self.junctions.append((self.rect.x + 20, self.rect.y + 20))

        if(wallSensed == 3):
            print(leftsensed)
            print(rightsensed)
            print(frontsensed)
            print(backsensed)

            if(not leftsensed):
                self.xSpeed = -self.xSpeed
            if(not rightsensed):
                self.xSpeed = -self.xSpeed
            if(not backsensed):
                self.ySpeed = -self.ySpeed
            if(not frontsensed):
                self.ySpeed = -self.ySpeed


            

        self.move(walls)
        time.sleep(.3)
        return wallSensed
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 5, 400, WHITE],
                 [0, 475, 480, 5, WHITE],
                 [475, 80, 5, 480, WHITE],
                 [0, 0, 480, 5, WHITE],
                 [0, 80, 160, 5, WHITE],
                 [240, 80, 160, 5, WHITE],
                 [80, 160, 240, 5, WHITE],
                 [80, 240, 80, 5, WHITE],
                 [240, 240, 160, 5, WHITE],
                 [160, 320, 160, 5, WHITE],
                 [0, 400, 80, 5, WHITE],
                 [160, 400, 80, 5, WHITE],
                 [400, 0, 5, 160, WHITE],
                 [400, 240, 5, 240, WHITE],
                 [80, 240, 5, 165, WHITE],
                 [160, 240, 5, 80, WHITE],
                 [240, 400, 5, 80, WHITE],
                 [320, 160, 5, 80, WHITE],
                 [320, 320, 5, 80, WHITE],
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([480, 480])
 
    # Set the title of the window
    pygame.display.set_caption('Maze Runner')
 
    # Create the robot paddle object
    robot = Robot(20, 420)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(robot)
    for sensor in robot.sensors:
        movingsprites.add(sensor)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    robot.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    robot.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    robot.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    robot.changespeed(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    robot.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    robot.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    robot.changespeed(0,5)
                if event.key == pygame.K_DOWN:
                    robot.changespeed(0, -5)
        if(robot.xSpeed == 0 & robot.ySpeed == 0):
            robot.changespeed(5,0)
        robot.tremaux(current_room.wall_list)
            
            

        if robot.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 480
                robot.rect.y = 0
            elif current_room_no == 2:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 480
                robot.rect.y = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 480
                robot.rect.y = 0
 
        if robot.rect.x > 480:
            if current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 0
                robot.rect.y = 420
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 0
                robot.rect.y = 420
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                robot.rect.x = 0
                robot.rect.y = 420
 
        # --- Drawing ---
        screen.fill(BLACK)
        
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        for junction in robot.junctions:
            pygame.draw.circle(screen, PURPLE, junction,15)
        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()