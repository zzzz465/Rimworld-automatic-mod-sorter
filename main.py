import downloader
import logging
import time
import Modmanager
import RWmanager
from time import sleep

Version = 0.5

DB = downloader.download_DB(Version)

formatter = logging.Formatter('{} [%(levelname)s] : %(message)s'.format(time.strftime('(%H:%M:%S)')))
log = logging.getLogger("RAMS")
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
file_handler = logging.FileHandler('RAMS_Log.txt', encoding='UTF-8')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.propagate = 0


if __name__ == '__main__':
    log.info('Initializing program...')

    log.info('downloading DB file...')
    Modmanager.ModBase.setDB(DB) #DB 파일 설정
    logging.info('download complete!')

    log.info('DB MOD COUNT : {}'.format(len(DB)))
    log.info('Latest DB updated date : {}'.format(DB['time']))

    log.info('select your ModsConfig.xml file')
    Modmanager.ModBase.ConfigXmldir = RWmanager.askfiledir('select ModsConfig.xml', [('ModsConfig.xml', '*.*')])

    log.info('select your Local mod folder.')
    localdir = RWmanager.askfolderdir()
    Modmanager.LoadMod(localdir)

    log.info('if you have any workshop mod, type Y')
    log.info("if you don't, type any key and press Enter")
    if str(input(' : ')).lower() == 'y':
        logging.info('select your workshop mod folder. folder number is 294100')
        workshopdir = RWmanager.askfolderdir()
        Modmanager.LoadMod(workshopdir, "Workshop")
    
    else:
        pass
    
    mods = list()
    for mod in Modmanager.Mod.MODs:
        if mod.MODkey in Modmanager.ModBase.ActiveModlist:
            mods.append(mod)

    log.info('sorting...')
    mods.sort(key=Modmanager.Mod.getOrderNum)
    log.info('sort complete.')

    log.debug(Modmanager.ModBase.ConfigXmldir)
    RWmanager.backup(Modmanager.ModBase.ConfigXmlfolderdir, 'ModsConfig.xml') # 백업 고치기
    #모드 배열을 XML에 올리는 것 추가하기
    #githubgist와 연동하기


    #RWmanager.backup() 백업은 마지막에
    



    

    


    
