# Created by a human
# when:
# 10/26/2015
# 3:55 PM
#
#
# --------------------------------------------------------------------
import pygame
import math


class Basic(pygame.sprite.Sprite):
    # a basic sprite for simple use
    # directly control the sprite with dx and dy
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface((16,16))
        self.surface.fill((120,120,120))
        self.rect = self.surface.get_rect()
        self.x = 100
        self.y = 100
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.check_screen_bounds()
        self.rect.center = (self.x, self.y)

    def check_screen_bounds(self):
        scrW = self.screen.get_width()
        scrH = self.screen.get_height()

        if self.x > scrW:
            self.x = 0
        if self.x < scrW:
            self.x = scrW
        if self.y > scrH:
            self.y = 0
        if self.y < scrH:
            self.y = scrH


class SuperSprite(pygame.sprite.Sprite):
    # An enhanced Sprite class
    # Use methods to change image, direction, speed
    # Will automatically travel in direction and speed indicated
    # Automatically rotates to point in indicated direction
    # Five kinds of boundary collision


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()

        #create constants
        self.WRAP = 0
        self.BOUNCE = 1
        self.STOP = 2
        self.HIDE = 3
        self.CONTINUE = 4

        #create a default text image as a placeholder
        #This will usually be changed by a setImage call
        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.imageMaster = self.font.render(">sprite>", True, (0, 0,0), (0xFF, 0xFF, 0xFF))
        self.image = self.imageMaster
        self.rect = self.image.get_rect()

        #create properties
        #most will be changed through method calls
        self.x = 200
        self.y = 200
        self.dx = 0
        self.dy = 0
        self.dir = 0
        self.rotation = 0
        self.speed = 0
        self.maxSpeed = 10
        self.minSpeed = -3
        self.boundAction = self.WRAP
        self.pressed = False
        self.oldCenter = (100, 100)
        self.states = {}
        self.currentState = "default"

    def update(self):
        self.oldCenter = self.rect.center
        self.checkEvents()
        self.rotate()
        self.calculateVector()
        self.calculatePosition()
        self.checkBounds()
        self.rect.center = (self.x, self.y)

    def checkEvents(self):
        # override event method in children classes
        pass

    def rotate(self):
        # PRIVATE METHOD
        #    change visual orientation based on
        #    rotation property.
        #    automatically called in update.
        #    change rotation property directly or with
        #    rotateBy(), setAngle() methods

        oldCenter = self.rect.center
        self.oldCenter = oldCenter
        self.image = pygame.transform.rotate(self.imageMaster, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

    def calculateVector(self):
        # calculates dx and dy based on speed, dir
        #   automatically called in update
        theta = self.dir / 180.0 * math.pi
        self.dx = math.cos(theta) * self.speed
        self.dy = math.sin(theta) * self.speed
        self.dy *= -1

    def calculatePosition(self):
        # calculates the sprites position adding
         #   dx and dy to x and y.
          #  automatically called in update
        self.x += self.dx
        self.y += self.dy

    def checkBounds(self):
        """ checks boundary and acts based on
            self.BoundAction.
            WRAP: wrap around screen (default)
            BOUNCE: bounce off screen
            STOP: stop at edge of screen
            HIDE: move off stage and wait
            CONTINUE: keep going at present course and speed

            automatically called by update
        """

        scrWidth = self.screen.get_width()
        scrHeight = self.screen.get_height()

        #create variables to simplify checking
        offRight = offLeft = offTop = offBottom = offScreen = False

        if self.x > scrWidth:
            offRight = True
        if self.x < 0:
            offLeft = True
        if self.y > scrHeight:
            offBottom = True
        if self.y < 0:
            offTop = True

        if offRight or offLeft or offTop or offBottom:
            offScreen = True

        if self.boundAction == self.WRAP:
            if offRight:
                self.x = 0
            if offLeft:
                self.x = scrWidth
            if offBottom:
                self.y = 0
            if offTop:
                self.y = scrHeight

        elif self.boundAction == self.BOUNCE:
            if offLeft or offRight:
                self.dx *= -1
            if offTop or offBottom:
                self.dy *= -1

            self.updateVector()
            self.rotation = self.dir

        elif self.boundAction == self.STOP:
            if offScreen:
                self.speed = 0

        elif self.boundAction == self.HIDE:
            if offScreen:
                self.speed = 0
                self.setPosition((-1000, -1000))

        elif self.boundAction == self.CONTINUE:
            pass

        else:
            # assume it's continue - keep going forever
            pass

    def setSpeed(self, speed):
        # immediately sets the objects speed to the
        # given value.

        self.speed = speed

    def speedUp(self, amount):
        # changes speed by the given amount
        #   Use a negative value to slow down

        self.speed += amount
        if self.speed < self.minSpeed:
            self.speed = self.minSpeed
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

    def setAngle(self, dir):
        """ sets both the direction of motion
            and visual rotation to the given angle
            If you want to set one or the other,
            set them directly. Angle measured in degrees
        """
        self.dir = dir
        self.rotation = dir

    def turnBy (self, amt):
        """ turn by given number of degrees. Changes
            both motion and visual rotation. Positive is
            counter-clockwise, negative is clockwise
        """
        self.dir += amt
        if self.dir > 360:
            self.dir = amt
        if self.dir < 0:
            self.dir = 360 - amt
        self.rotation = self.dir

    def rotateBy(self, amt):
        """ change visual orientation by given
            number of degrees. Does not change direction
            of travel.
        """
        self.rotation += amt
        if self.rotation > 360:
            self.rotation = amt
        if self.rotation < 0:
            self.rotation = 360 - amt

    def setImage (self, image):
        """ loads the given file name as the master image
            default setting should be facing east.  Image
            will be rotated automatically """
        self.imageMaster = pygame.image.load(image)
        self.imageMaster = self.imageMaster.convert()

    def setDX(self, dx):
        """ changes dx value and updates vector """
        self.dx = dx
        self.updateVector()

    def addDX(self, amt):
        # adds amt to dx, updates vector
        self.dx += amt
        self.updateVector()

    def setDY(self, dy):
        # changes dy value and updates vector
        self.dy = dy
        self.updateVector()

    def addDY(self, amt):
        # adds amt to dy and updates vector
        self.dy += amt
        self.updateVector()

    def setComponents(self, components):
        # expects (dx, dy) for components
        # change speed and angle according to dx, dy values

        (self.dx, self.dy) = components
        self.updateVector()

    def setBoundAction (self, action):
        # sets action for boundary.  Values are
        #   self.WRAP (wrap around edge - default)
        #   self.BOUNCE (bounce off screen changing direction)
        #   self.STOP (stop at edge of screen)
        #   self.HIDE (move off-stage and stop)
        #   self.CONTINUE (move on forever)
        #   Any other value allows the sprite to move on forever
        self.boundAction = action

    def setPosition (self, position):
        # place the sprite directly at the given position
        #   expects an (x, y) tuple
        (self.x, self.y) = position

    def moveBy (self, vector):
        # move the sprite by the (dx, dy) values in vector
        # automatically calls checkBounds. Doesn't change
        # speed or angle settings.

        (dx, dy) = vector
        self.x += dx
        self.y += dy
        self.checkBounds()

    def forward(self, amt):
        """ move amt pixels in the current direction
            of travel
        """

        #calculate dx dy based on current direction
        radians = self.dir * math.pi / 180
        dx = amt * math.cos(radians)
        dy = amt * math.sin(radians) * -1

        self.x += dx
        self.y += dy

    def addForce(self, amt, angle):
        # apply amt of thrust in angle.
        #    change speed and dir accordingly
        #    add a force straight down to simulate gravity
        #    in rotation direction to simulate spacecraft thrust
        #    in dir direction to accelerate forward
        #    at an angle for retro-rockets, etc.

        #calculate dx dy based on angle
        radians = angle * math.pi / 180
        dx = amt * math.cos(radians)
        dy = amt * math.sin(radians) * -1
        self.dx += dx
        self.dy += dy
        self.updateVector()

    def updateVector(self):
        #calculate new speed and angle based on dx, dy
        #call this any time you change dx or dy

        self.speed = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))

        dy = self.dy * -1
        dx = self.dx

        radians = math.atan2(dy, dx)
        self.dir = radians / math.pi * 180

    def setSpeedLimits(self, max, min):
        # determines maximum and minimum
        #    speeds you will allow through
        #    speedUp() method.  You can still
        #    directly set any speed you want
        #    with setSpeed() Default values:
        #        max: 10
        #        min: -3

        self.maxSpeed = max
        self.minSpeed = min

    def dataTrace(self):
        #    utility method for debugging
        #    print major properties
        #    extend by adding properties

        print "x: %d, y: %d, speed: %.2f, dir: %.f, dx: %.2f, dy: %.2f" % \
              (self.x, self.y, self.speed, self.dir, self.dx, self.dy)

    def mouseDown(self):
        # boolean function. Returns True if the mouse is
        #    clicked over the sprite, False otherwise

        self.pressed = False
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.pressed = True
        return self.pressed

    def clicked(self):
        """ Boolean function. Returns True only if mouse
            is pressed and released over sprite
        """
        released = False
        if self.pressed:
            if pygame.mouse.get_pressed() == (0, 0, 0):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    released = True
            return released

    def collidesWith(self, target):
        # boolean function. Returns True if the sprite
        #   is currently colliding with the target sprite,
        #   False otherwise

        collision = False
        if self.rect.colliderect(target.rect):
            collision = True
        return collision

    def collidesGroup(self, target):
        # wrapper for pygame.sprite.collideany
        #   simplifies checking sprite - group collisions
        #   returns result of collision check (sprite from group
        #   that was hit or None)

        collision = pygame.sprite.spritecollideany(self, target)
        return collision

    def distanceTo(self, point):
        # returns distance to any point in pixels
        #    can be used in circular collision detection
        (pointx, pointy) = point
        dx = self.x - pointx
        dy = self.y - pointy

        dist = math.sqrt((dx * dx) + (dy * dy))
        return dist

    def dirTo(self, point):
        # returns direction (in degrees) to a point

        (pointx, pointy) = point
        dx = self.x - pointx
        dy = self.y - pointy
        dy *= -1

        radians = math.atan2(dy, dx)
        dir = radians * 180 / math.pi
        dir += 180
        return dir

    def drawTrace(self, color=(0x00, 0x00, 0x00)):
        # traces a line between previous position
        #   and current position of object

        pygame.draw.line(self.scene.background, color, self.oldCenter,
                         self.rect.center, 3)
        self.screen.blit(self.scene.background, (0, 0))

    def addState(self, stateName, stateImageFile):
        # Creates a new sprite state with the associated name
        # and image. Useful to build multi-state sprites.
        # load the image
        tempImage = pygame.image.load(stateImageFile)
        tempImage.convert()
        self.states[stateName] = tempImage

    def setState(self, stateName):
        """ attempts to set the sprite to the indicated state
            (image)
        """
        self.imageMaster = self.states[stateName]
        self.rect = self.imageMaster.get_rect()
        self.currentState = stateName

    def getState(self):
        """ returns the current state name
            (default if no states have been explicitly set)
        """
        return self.currentState


