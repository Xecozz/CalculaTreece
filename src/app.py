"""
The pygame app
"""
import pygame


class App:
    """
    Main class for the app
    """

    def __init__(self, screen1):
        super().__init__()
        self.screen = screen1
        self.running = True
        self.clock = pygame.time.Clock()
        self.title = "CalculaTreece"
        self.icon = pygame.image.load("icon.ico")
        self.font = pygame.font.SysFont("Intro", 55)

    def handle_events(self):
        """
        Handle events
        """
        for event in pygame.event.get():  # get all events
            if event.type == pygame.QUIT:  # if the event is QUIT
                self.running = False  # stop the loop

    def display(self):
        """
        Global display of the app
        """
        # Background
        self.screen.fill("#E7E7E7")  # fill the screen with grey
        pygame.display.set_caption(self.title)  # set the title of the window
        pygame.display.set_icon(self.icon)  # set the icon of the window

    def button_number_0(self):
        button_0 = Button("0", 100, 75, (105, 440), self.screen)
        button_0.draw()
        Value = TextBox(self.screen)
        if button_0.check_click():
            print("0")
            Value.draw()

    def button_number_1(self):
        button_1 = Button("1", 100, 75, (0, 360), self.screen)
        button_1.draw()
        if button_1.check_click():
            print("1")

    def button_number_2(self):
        button_2 = Button("2", 100, 75, (105, 360), self.screen)
        button_2.draw()
        if button_2.check_click():
            print("2")

    def button_number_3(self):
        button_3 = Button("3", 100, 75, (210, 360), self.screen)
        button_3.draw()
        if button_3.check_click():
            print("3")

    def button_number_4(self):
        button_4 = Button("4", 100, 75, (0, 280), self.screen)
        button_4.draw()
        if button_4.check_click():
            print("4")

    def button_number_5(self):
        button_5 = Button("5", 100, 75, (105, 280), self.screen)
        button_5.draw()
        if button_5.check_click():
            print("5")

    def button_number_6(self):
        button_6 = Button("6", 100, 75, (210, 280), self.screen)
        button_6.draw()
        if button_6.check_click():
            print("6")

    def button_number_7(self):
        button_7 = Button("7", 100, 75, (0, 200), self.screen)
        button_7.draw()
        if button_7.check_click():
            print("7")

    def button_number_8(self):
        button_8 = Button("8", 100, 75, (105, 200), self.screen)
        button_8.draw()
        if button_8.check_click():
            print("8")

    def button_number_9(self):
        button_9 = Button("9", 100, 75, (210, 200), self.screen)
        button_9.draw()
        if button_9.check_click():
            print("9")

    def button_operation_add(self):
        button_add = Button("+", 100, 75, (315, 360), self.screen)
        button_add.draw()
        if button_add.check_click():
            print("+")

    def button_operation_sub(self):
        button_sub = Button("-", 100, 75, (315, 280), self.screen)
        button_sub.draw()
        if button_sub.check_click():
            print("-")

    def button_operation_mul(self):
        button_mul = Button("*", 100, 75, (315, 200), self.screen)
        button_mul.draw()
        if button_mul.check_click():
            print("*")

    def button_operation_div(self):
        button_div = Button("/", 100, 75, (315, 120), self.screen)
        button_div.draw()
        if button_div.check_click():
            print("/")

    def button_operation_equal(self):
        button_equal = Button("=", 100, 75, (315, 440), self.screen)
        button_equal.draw_equal_button()
        if button_equal.check_click():
            print("=")

    def button_operation_clear(self):
        button_clear = Button("C", 100, 75, (210, 120), self.screen)
        button_clear.draw()
        if button_clear.check_click():
            print("C")

    def run(self):
        """
        Main loop
        """
        textbox = TextBox(self.screen)
        while self.running:  # loop until the user clicks the close button
            self.handle_events()
            self.display()
            self.clock.tick(60)
            if self.running:
                self.button_number_0()
                self.button_number_1()
                self.button_number_2()
                self.button_number_3()
                self.button_number_4()
                self.button_number_5()
                self.button_number_6()
                self.button_number_7()
                self.button_number_8()
                self.button_number_9()
                self.button_operation_add()
                self.button_operation_sub()
                self.button_operation_mul()
                self.button_operation_div()
                self.button_operation_equal()
                self.button_operation_clear()
            textbox.draw()

            pygame.display.flip()  # update the display


class Button:
    def __init__(self, text, width, height, pos, screen):
        self.pressed = False
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#808080'
        self.screen = screen

        # text
        self.text_surf = gui_font.render(text, True, '#000000')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, 0, 3)
        self.screen.blit(self.text_surf, self.text_rect)
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.screen, 'Black', self.top_rect, 3, 3)
                self.screen.blit(self.text_surf, self.text_rect)
                return 'Number Pressed'
            else:
                pygame.draw.rect(self.screen, '#9E9E9E', self.top_rect, 0, 3)
                self.screen.blit(self.text_surf, self.text_rect)

    def draw_equal_button(self):
        pygame.draw.rect(self.screen, 'Cyan', self.top_rect, 0, 3)
        self.screen.blit(self.text_surf, self.text_rect)
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.screen, '#0072EB', self.top_rect, 3, 3)
                self.screen.blit(self.text_surf, self.text_rect)
            else:
                pygame.draw.rect(self.screen, '#00B6EB', self.top_rect, 0, 3)
                self.screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()  # get the mouse position
        if self.top_rect.collidepoint(mouse_pos):  # check if the mouse position is over the button
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                return True
            else:
                if self.pressed:
                    self.pressed = False


class TextBox:
    def __init__(self, screen):
        self.screen = screen
        self.text = ''
        self.text_surf = gui_font.render(self.text, True, 'Black')
        self.text_rect = self.text_surf.get_rect(center=(210, 50))

    def draw(self):
        pygame.draw.rect(self.screen, '#5882D9', (0, 0, 420, 100), 0, 3)
        self.screen.blit(self.text_surf, self.text_rect)


pygame.init()
gui_font = pygame.font.Font(None, 50)
