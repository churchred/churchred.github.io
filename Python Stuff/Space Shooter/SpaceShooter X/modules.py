

class Button:
    def __init__(self, width, height, x, y, color, hover_color, click_color, text, text_size, text_color):
        self.w = width
        self.h = height
        self.x = x
        self.y = y

        self.col = btn_color
        self.hov_col = btn_hov_color
        self.text_col = text_color
        self.name = text
        self.text_size = text_size
        self.click_col = btn_presses_color

        self.test_1 = False
        self.test_2 = False
        self.test_3 = False

    def draw(self):
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(SCREEN, self.col, (self.x, self.y, self.w, self.h))
        # Checks if Mouse is hovering over the button
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(SCREEN, self.hov_col, (self.x, self.y, self.w, self.h))
            if self.test_3:
                pygame.draw.rect(SCREEN, self.click_col, (self.x, self.y, self.w, self.h))
            text(self.name, self.text_size, self.text_col, self.x + self.text_size / 2, self.y + self.text_size)
            self.test_1 = True
            if self.click():
                return True
        else:
            text(self.name, self.text_size, self.text_col, self.x + self.text_size / 2, self.y + self.text_size)
            self.test_1 = False
            self.test_2 = False
            self.test_3 = False

    def click(self):
        click = pygame.mouse.get_pressed()

        if click[0] == 0:
            self.test_2 = True

        if self.test_2:
            if click[0] == 1:
                self.test_3 = True

        if self.test_3:
            if click[0] == 0:
                self.test_1 = False
                self.test_2 = False
                self.test_3 = False
                return True
