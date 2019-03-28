import logging
import curses
from time import sleep
try:
    from core import Modmanager, downloader, RWmanager, Loghandler
except:
    import Modmanager, downloader, RWmanager, Loghandler
screen = curses.initscr()

def rootscr(screen):
    '''
    get a screen and (type object) mod list.
    make a screen with that.
    Refer to https://gist.github.com/claymcleod/b670285f334acd56ad1c
    '''
    cursor_x = 0
    cursor_y = 0

    #initial setting.
    curses.noecho()
    screen.keypad(True)
    curses.cbreak()

    curses.resize_term(120,50)

    # Clear and refresh the screen for a blank canvas
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

def listscr(screen, DB, MODs):

    #make list, [[page number, number, modname, grated number, Color]]
    # 한 줄에 35칸정도
    list1 = list()
    
    page = 1
    number = 1

    lty = 1 #left top y in a box
    ltx = 2 #left top x in a box
    
    screen.move(lty, ltx) #don't forget there is a border.
    cursor = [lty,ltx]# y x
    for line in list1:
        screen.attron(line[4])
        message = "{} : {}".format(line[2], line[3])
        screen.addstr(message.rjust(35, " "))
        screen.attroff(line[4])

        cursor[0] += 1

        screen.move(cursor[0], cursor[1])
        screen.refresh()
        sleep(0.1)
        screen.getstr()

    
    screen.refresh()
    screen.getstr()

def makelist(DB):
    '''
    '''
    MODs = Modmanager.Mod.MODs
    page = 1
    number = 1

    #each page has 20 mods.
    list1 = list()
    for MOD in MODs:
        if number == 21:
                    page += 1
                    number = 1
        
        if MOD.MODname in DB: # if mod is in DB
            list1.append([page, number, MOD.MODname, 0.0, curses.COLOR_GREEN])
        
        else: # if mod isn't in DB
            list1.append([page, number, MOD.MODname, 0.0, curses.COLOR_RED])
        
        number += 1

    return list1



def showlist(screen, page):

    lty = 1 #left top y in a box
    ltx = 2 #left top x in a box
    screen.move(lty, ltx) #don't forget there is a border.
    cursor = [lty,ltx]# y x
    for line in list1:
        screen.attron(line[4])
        message = "{} : {}".format(line[2], line[3])
        screen.addstr(message.rjust(35, " "))
        screen.attroff(line[4])

        cursor[0] += 1

        screen.move(cursor[0], cursor[1])
    
        #if cursor[0] == 

#def statusbar(screen):

        


if __name__ == '__main__':
    #set logs
    '''
    log = logging.getLogger("RAMS")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S") #TODO change to more readable format.
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)

    DB = downloader.download_DB()
    Modmanager.ModBase.setinit()

    screen_root = curses.initscr()
    screen_root.border(0)
    rootscr(screen_root)

    height, width = screen_root.getmaxyx()

    screen_list = curses.newwin(height-3, width-20, 2, 0)
    screen_list.border()
    
    listscr(screen_list, DB, Modmanager.Mod.MODs)
    '''

    screen_root = curses.initscr()

    curses.resize_term(120,50) # resize it to 120, 50

    rootscr(screen_root)
    screen_root.getstr()
    