import curses

class screen:
    '''
    set common value of screen\n
    every sub class should run __init__ after creating newwin or something.
    '''
    def __init__(self, screen):
        self.max_y, self.max_x = screen.getmaxyx()


class scr_frame(screen):

    def __init__(self, height, width, begin_y, begin_x):
        self.screen = curses.newwin(height, width, begin_y, begin_x)
        self.screen.border() #make border.

        super().__init__(self.screen)

        self.scr_list = []

    def add_screen(self, screen):
        self.scr_list.append(screen)



class scr_list(screen):
    def __init__(self, height, width, begin_y, begin_x):
        self.screen = curses.newwin(height, width, begin_y, begin_x)

        super().__init__(self.screen)
        