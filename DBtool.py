from core import downloader, Modmanager, RWmanager
import logging

formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S") #TODO change to more readable format.
log = logging.getLogger("RAMS.DBtool")
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.propagate = 0
logfile_handler = logging.FileHandler('RAMS.DBtool.log')
log.addHandler(logfile_handler)

Toolversion = 0.1 # seperate from Main program.

if __name__ == '__main__':
    log.info('initializing DB tool...')

    DB = downloader.download_DB()
    Modmanager.ModBase.setDB(DB)

    Modmanager.ModBase.setinit()

    #Modmanager.ModBase.\    