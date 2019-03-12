import logging
import logging.handlers
import time

import finder
import downloader

isworkshop = bool()
Version = 0.5

class setlog(self):
    def __init__(self):
        self.log = logging.getLogger('RAMS')
        self.log.setLevel(logging.INFO) #기본 세팅

        self.formatter = logging.Formatter(time.strftime('%d %M %S') + ' [%(levelname)s] : %(message)s')

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.format(formatter)
        self.log.addHandler(stream_handler)

        self.file_handler = logging.FileHandler()
        self.file_handler.format(formatter)
        self.log.addHandler(file_handler)

def set_dir(dir1, dir2, dir3): #로컬 / 워크샵 / config파일
    logging.info('select your local mod folder.')
    logging.info('default directory : /steam/steamapps/common/Rimworld/Mods')
    dir1 = finder.finder_folder()
    
    if isworkshop == True:
        logging.info('select your workshop mod folder')
        logging.info('default directory : /steam/steamapps/workshop/294100')
        dir2 = finder.finder_folder()

    logging.info('select your rimworld config file.')
    dir3 = finder.finder_folder()

def get_DB(DB, Version):
    DB = downloader.download_DB(DB, Version)







if __name__ == '__main__':
    log = setlog()
    log.info('initializing Program...')

    DB = dict()
    get_DB(DB, Version)

    logging.info('MOD IN DB : {}'.format(len(DB)))
    logging.info('DB updated date : {}'.format(DB['time']))

    

