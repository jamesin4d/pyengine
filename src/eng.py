# Created by a human
# when:
# 10/26/2015
# 10:50 AM
#
#
# --------------------------------------------------------------------
import sys
import pygame


class FiniteStateMachine(object):

    def __init__(self):
        self.current_state = State()
        self.states = []

    def run(self):
        self.states = [self.current_state]
        while self.states:
            self.current_state = self.states.pop()
            if self.current_state.paused:
                self.current_state.unpause()

            next_state, paused = self.current_state.mainloop()
            if self.current_state.kill_prev and self.states:
                self.states.pop()
            if paused:  # paused states are kept
                self.states.append(self.current_state)
            if next_state:
                self.states.append(next_state)


class State(object):
    def __init__(self):
        self.done = False
        self.next_state = None
        self.clock = pygame.time.Clock()
        self.paused = False
        self.kill_prev = False
        self.screen = pygame.display.get_surface()

    def reinit(self):
        pass

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False
        self.done = False
        self.next_state = None

    def main_start(self):
        pass

    def mainloop(self):
        self.main_start()
        while not self.done:
            self.check_events()
            self.check_collisions()
            self.update_screen()
            self.tick()
            pygame.event.pump()
        return self.next_state, self.paused

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.quit()

    def check_collisions(self):
        pass

    def update_screen(self):
        pass

    def tick(self):
        self.clock.tick(30)

    def quit(self):
        self.done = True
        self.screen.fill((0,0,0))
        return self.next_state, self.paused

    def close_game(self):
        sys.exit(0)