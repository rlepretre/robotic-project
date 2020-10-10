import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))     # fill the background white 
background = background.convert()  # prepare for faster blitting
 
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


for wall in walls:
    pygame.draw.line(background, (255,0,0), wall[0],wall[1],2)

pygame.draw.rect(background, (0,0,255),(0,80,60,60),2)

class Player(): #pygame.sprite.Sprite
 
    xSpeed = 0
    ySpeed = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom




 
#------- blit the surfaces on the screen to make them visible
screen.blit(background, (0,0))     # blit the background on the screen (overwriting all)
clock = pygame.time.Clock()
mainloop = True
FPS = 30 # desired framerate in frames per second. try out other values !
playtime = 0.0
 
while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
    pygame.display.set_caption("Maze Simulation")
    pygame.display.flip()      # flip the screen like in a flipbook
print("this 'game' was played for %.2f seconds" % playtime)