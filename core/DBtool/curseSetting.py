import curses

def curses_init():
    '''
    return curses root window.
    and do initial settings.
    '''
    #init screen
    screen = curses.initscr()

    #set sttings.
    curses.noecho()
    screen.keypad(True)
    curses.cbreak()

    #change size to ideal size.
    curses.resize_term(120,50)

    #clear screen for caution's sake
    screen.clear()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # like blue
    curses.init_color(curses.COLOR_RED, 1000, 220, 300) #change to bright red, curses use 0~1000 digit RGB code. R G B
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    height, width = screen.getmaxyx() # get max height, width

    #declaration of strings.
    y, x =screen.getyx()
    cursorlocation = '{} {}'.format(y,x)
    str_help = '"ESC" to save & quit | "ENTER" to modify, set number.\n"UP/DOWN Arrow keys" to move | "LEFT/RIGHT Arrow keys" to move page.'
    str_status = 'Number of MODs not in DB : {} | Number of Mods that you just Registered to DB : {} | cursor location = {}'.format(cursorlocation, cursorlocation, cursorlocation)

    #Rendering declaration
    screen.attron(curses.color_pair(3))
    screen.addstr(height-1, 0, str_status)
    screen.addstr(height-1, len(str_status), " " *  (width - len(str_status) - 1))
    screen.attroff(curses.color_pair(3))

    screen.attron(curses.color_pair(1))
    screen.addstr(0, 0, str_help)
    screen.attroff(curses.color_pair(1))

    #move cursor
    screen.move(2, 0)

    #text message
    #screen.attron(curses.color_pair(2))
    #screen.addstr('test text message(red)')
    #screen.attroff(curses.color_pair(2))

    #refresh the screen
    screen.refresh()

    return screen

