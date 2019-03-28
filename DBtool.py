from core import downloader, Modmanager, RWmanager, Loghandler
import logging
import curses

Toolversion = 0.1 # seperate from Main program.

stdscr = curses.initscr()

formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S")
log = Loghandler.initLog('RAMS', logging.DEBUG)
stream_handler = Loghandler.CursesHandler(stdscr)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)

def overlap_remove(DB, Modlist):
    '''
    accept DB and Modlist
    return Mod list with overlapping mod removed
    '''
    list1 = list()
    for x in Modlist:
        if x.MODname in DB:
            continue
        
        else:
            list1.append(x)
    
    return x

def main():
    begin_x = 0
    begin_y = 7
    maxheight, maxwidth = stdscr.getmaxyx()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    window = curses.newwin(maxheight, maxwidth, 0, 0)

        
if __name__ == '__main__':
    log.info('initializing DB tool...')

    DB = downloader.download_DB()
    Modmanager.ModBase.setDB(DB)

    Modmanager.ModBase.setinit()

    Mods = overlap_remove(DB, Modmanager.Mod.MODs)

    