
def start_page():
    print("start page ")
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    arrow.draw()


class Arrow():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


arrow = Arrow(screen_width // 2 - 100, screen_height // 2 - 100, arrow_img)

# draw Menu button
class Menu():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


    if game_over == False and flying == False and start == True:
        arrow.draw()
        start_page()


    if game_over == True:
        if button_2.draw() == True:
            print("hi")
            game_over = False
            main = start_page()
            start = True
            score = reset_game()

# create menu button instance
button_2 = Menu(screen_width // 2 - 50, screen_height // 2 - 50, menu_img)
