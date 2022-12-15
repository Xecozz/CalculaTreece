"""
The main entry
"""
import pygame
import sys

import automaton
import calculator
import transformations
import trees


class App:
    def __init__(self, screen1):
        self.screen = screen1
        self.running = True
        self.clock = pygame.time.Clock()
        self.rectangle = pygame.Rect(150, 50, 500, 500)
        self.title = "CalculaTreece"
        self.font = pygame.font.SysFont("Arial", 36)

    def handle_events(self):  # handle events
        for event in pygame.event.get():  # get all events
            if event.type == pygame.QUIT:  # if the event is QUIT
                self.running = False  # stop the loop

    def display(self):
        # Background
        self.screen.fill("grey")  # fill the screen with grey
        pygame.display.set_caption(self.title)  # set the title of the window

        # Content
        text = self.font.render("Test", True, "black")
        pygame.draw.rect(self.screen, "red", self.rectangle)
        self.screen.blit(text, (0, 0))

        # Update
        pygame.display.flip()

    def run(self):
        while self.running:  # loop until the user clicks the close button
            self.handle_events()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((800, 600))
app = App(screen)
app.run()
pygame.quit()
