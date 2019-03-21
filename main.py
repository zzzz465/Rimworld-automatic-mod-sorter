import logging
import time
from time import sleep
import sys
import os
import webbrowser

from core import *

currentdir = os.getcwd()
Version = 0.51 #dev

formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S") #TODO change tomore readable format.
log = logging.getLogger("RAMS")
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.propagate = 0
logfile_handler = logging.FileHandler('RAMS.log')
log.addHandler(logfile_handler)

logcollect = '''compare your mods with online DB, and get mods which are not on the DB
'''

weblogurl = 'https://gist.github.com/RAMSlog'

if __name__ == '__main__':
    log.info('Initializing program...')
    sleep(0.5) #TODO I'm trying to add sleep function between every log message with decorator, closure or something else.
    DB = downloader.download_DB() # GET DB from server
    Modmanager.ModBase.setDB(DB) # DB 파일 설정

    try: #to give any important messages.
        log.info(DB['message'])
        sleep(3)
    except:
        pass

    log.info('current version = {}'.format(Version))

    #버전체크
    if Version < DB['Version']:
        log.info('latest version > {}'.format(DB['Version']))
        log.info('please update to latest version.')
        log.info('program will be closed in 5 seconds...')
        sleep(5)
        sys.exit(0)
    sleep(0.5)# this is my stupid decision.

    log.info('DB MOD COUNT : {}'.format(len(DB)))
    log.info('Latest DB updated date : {}'.format(DB['time']))
    sleep(2)

    Modmanager.ModBase() #run __init__

    sleep(1)
    if str(input('Load Workshop Mod? Y/N > ')).lower() == 'y':
        logging.info('select your workshop mod folder. folder number is 294100')
        workshopdir = RWmanager.askfolderdir()
        Modmanager.LoadMod(workshopdir, "Workshop")
    
    else:
        pass
    
    log.info('current loaded mod number : {}'.format(len(Modmanager.Mod.MODs)))
    while True:
        a = input('Activate All? Y/N > ')
        if a.isalpha():
            if a.lower() == 'y':
                Modmanager.Mod.ActiveModlist = list() # 활성화 리스트 초기화
                for x in Modmanager.Mod.MODs:
                    Modmanager.Mod.ActiveModlist.append(x.MODkey) #로드된 모드를 전부 활성화 리스트에 집어넣음
                
                break
            
            elif a.lower() == 'n':
                break
        
        else:
            log.info('input Y/N, not {}'.format(a))
                


    sleep(1)
    log.info('sorting...')
    Modmanager.Mod.Sort()
    mods = Modmanager.Mod.list3
    log.info('sort complete.')

    RWmanager.backup(Modmanager.ModBase.Configxmlfolderpath, 'ModsConfig.xml') #backup file
    Modmanager.update_config(Modmanager.ModBase.Configxmlfolderpath, mods) #write ModsConfig.xml and save.

    log2 = logging.getLogger('RAMS.UploadLog')
    file_handler = logging.FileHandler('RAMS.log', encoding='UTF-8', mode='w')
    log2.addHandler(file_handler) #base

    #TODO add color distinction and more readable format.
    log.info('Your activated mod list\n----------')
    for x in mods: 
        log2.info(x.MODname)
        sleep(0.05)

    nMods = Modmanager.Mod.list2 + Modmanager.Mod.list4 #should move to ModManager class method
    if nMods != []:#should
        log_upload = 'missing mod in DB'
        log2.info('Missing mode in DB (need manual activation)\n')
        log2.info('---LOG START---')
        for x in nMods:
            log2.info(x.MODname)
            log_upload = log_upload + '\n{}'.format(x.MODname)
            sleep(0.05)
        log2.info('---LOG END---\n')
    sleep(1)
    log.info('The above log will be sent to the server if you want.')
    log.info('Help the developer improve the program by uploading a DB')
    print('log will collect :\n {}'.format(logcollect)) #let users know what data will be upload to github gist.

    while True:
        a = input('upload it? Y/N > ')
        if a.isalpha():
            if a.lower() == 'y':
                from upload import gitupload
                gitupload(log_upload, DB['token'])
                sleep(5) # wait for gist update
                webbrowser.open(weblogurl) # show log file.
                log.info('exit in 5 seconds...')
                sys.exit(0)
            
            elif a.lower() == 'n':
                log.info('exit in 5 seconds...')
                sleep(4)
                sys.exit(0)
        
        else:
            log.info('input Y/N, not {}'.format(a))
    #githubgist와 연동하기
    



    

    


    
