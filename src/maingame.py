# Created by a human
# when:
# 10/26/2015
# 10:51 AM
#
#
# --------------------------------------------------------------------

from states import splash
from eng import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (750, 40)

def main():
    window_width = 800
    window_height = 480
    display = (window_width, window_height)
    #DEPTH = 32
    #FLAGS = 0
    #CAMERA_SLACK = 32
    pygame.init()
    pygame.display.set_mode(display)
    e = FiniteStateMachine()
    e.current_state = splash.SplashScreen()
    e.run()
