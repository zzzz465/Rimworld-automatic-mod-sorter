import curses
import _curses
import logging
from time import sleep

formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S")
class CursesHandler(logging.Handler):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def emit(self, record):
        try:
            msg = self.format(record)
            screen = self.screen
            # issue 35046: merged two stream.writes into one.
            fs = "\n%s"
            
            screen.addstr(fs % msg)
            screen.refresh()

        except Exception:
            self.handleError(record)

def initLog(name, LogLevel):
    '''
    LogLevel = Logging.INFO, WARNING, DEBUG or ERROR
    set basic logging.
    return log
    '''
    logger = logging.getLogger('{}'.format(name))
    logger.setLevel(LogLevel)
    logger.propagate = 0

    logfile_handler = logging.FileHandler('RAMS.file')
    logger.addHandler(logfile_handler)

    return logger

if __name__ == '__main__':
    '''
    log = initLog('test', logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)

    log.info('test message.')
    '''

    
    try:
        stdscr = curses.initscr()
        stdscr.addstr('testing logging with module curses')

        screen_handler = CursesHandler(stdscr)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S")
        screen_handler.setFormatter(formatter)

        log = logging.getLogger()
        log.addHandler(screen_handler)
        log.setLevel(logging.INFO)

        for i in range(10):
            log.info('test message %d', i)
            sleep(1)

    except:
        pass

    finally:
        input('b')
    