#-*- coding:utf-8 -*-
import json
import os
import shutil
import tempfile
import zipfile
import sys
from time import sleep
from urllib.request import urlopen
import logging

DB_url = 'https://raw.githubusercontent.com/zzzz465/Rimworld-automatic-mod-sorter/master/db_template.json'

log = logging.getLogger('RAMS.downloader')

def download_DB(): #shakeyourbunny's code. thank you!
    try:
        '''Return latest DB file type <dict>
        '''
        log.info('fetching latest DB file from server...')
        log.info('please allow firewall internet connection.')
        sleep(1)
        with urlopen(DB_url) as jsonurl:
            dbrawdata = jsonurl.read()
        
        log.info('DB download complete!')
        
        return json.loads(dbrawdata)

    except:
        try:
            log.warning('cannot download DB from server. loading local DB files...')
            currentpath = os.getcwd() # 설마..

            from core import RWmanager
            xmlpath = RWmanager.askfiledir(titlename="select DB_template.json", filetype=[('*.*', '*.*')])
            os.chdir(os.path.dirname(xmlpath))
            with open('DB_template.json', mode='r') as jsonlocal:
                dbrawdata = jsonlocal.read()

            os.chdir(currentpath) #FIXME change to more better code.

            return json.loads(dbrawdata)
        
        except:
            log.error('cannot found DB file from local. exit program...')
            sys.exit(0)

if __name__ == '__main__':
    DBtest = download_DB()
    for x in DBtest:
        print(x)
    print(type(DBtest))