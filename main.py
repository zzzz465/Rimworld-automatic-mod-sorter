import downloader
import logging
import time
import Modmanager
import RWmanager
from time import sleep
import sys
import upload
import os

currentdir = os.getcwd()


Version = 0.5

DB = downloader.download_DB(Version)

formatter = logging.Formatter('%(asctime)s - [%(levelname)s] : %(message)s')
log = logging.getLogger("RAMS")
log.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.propagate = 0
logfile_handler = logging.FileHandler('program.log')
log.addHandler(logfile_handler)

if __name__ == '__main__':
    log.info('Initializing program...')
    sleep(1) # I'm trying to add sleep function between every log message with decorator, closure or something else.

    log.info('downloading DB file...')
    Modmanager.ModBase.setDB(DB) #DB 파일 설정
    logging.info('download complete!')
    sleep(1)# this is my stupid decision.

    log.info('DB MOD COUNT : {}'.format(len(DB)))
    log.info('Latest DB updated date : {}'.format(DB['time']))
    sleep(1)

    log.info('select your ModsConfig.xml file')
    Modmanager.ModBase.ConfigXmldir = RWmanager.askfiledir('select ModsConfig.xml', [('ModsConfig.xml', '*.*')])
    sleep(1)

    log.info('select your Local mod folder.')
    localdir = RWmanager.askfolderdir()
    Modmanager.LoadMod(localdir)

    sleep(1)
    log.info('if you have any workshop mod, type Y')
    log.info("if you don't, type any key and press Enter")
    if str(input(' : ')).lower() == 'y':
        logging.info('select your workshop mod folder. folder number is 294100')
        workshopdir = RWmanager.askfolderdir()
        Modmanager.LoadMod(workshopdir, "Workshop")
    
    else:
        pass


    sleep(1)
    log.info('sorting...')
    Modmanager.Mod.Sort()
    mods = Modmanager.Mod.list3
    log.info('sort complete.')

    dir1 = Modmanager.ModBase.ConfigXmldir[:len(Modmanager.ModBase.ConfigXmldir)-15]
    RWmanager.backup(dir1, 'ModsConfig.xml') 

    Modmanager.update_config(dir1, mods)

    log2 = logging.getLogger('UploadLog')
    file_handler = logging.FileHandler('RAMS.log', encoding='UTF-8', mode='w')
    log2.addHandler(file_handler)

    log.info('Your activated mod list\n----------')
    for x in mods:
        log.info(x.MODname)

    if Modmanager.Mod.list2 != []:
        log.info('Missing mode in DB (need manual activation)\n------------')
        for x in Modmanager.Mod.list2:
            log.info(x.MODname)


    os.chdir(currentdir)

    #githubgist와 연동하기
    



    

    


    
