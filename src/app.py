import pygame


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
        # pygame.draw.rect(self.screen, "red", self.rectangle)
        self.screen.blit(text, (0, 0))

        # Update

    def draw_button(self): # dessine les boutons de la calculatrice
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(self.screen, "white", (i * 100, j * 100, 100, 100), 1)
        number = self.font.render("1", True, "black")
        self.screen.blit(number, (165, 10))

    def run(self):
        while self.running:  # loop until the user clicks the close button
            self.handle_events()
            self.display()
            self.clock.tick(60)
            self.draw_button()
            pygame.display.flip()  # update the display


class Bouton:
    def __init__(self, x, y, width, height, text):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("Arial", 36)
        self.text = self.font.render(text, True, "black")
        self.screen = pygame.display.set_mode((800, 600))

    def display(self):
        pygame.draw.rect(self.screen, "red", self.rectangle)
        self.screen.blit(self.text, (0, 0))
        pygame.display.flip()


pygame.init()