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

DB = dict()

def download_DB(Ver): # DB 다운받아서, DB 반환, 버전 체크도 함께
    global DB
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)
    with urlopen(DB_url) as res:
        res_data = res.read()

        with open('./DB_template.json', 'wb') as f:
            f.write(res_data)
 
    with open('db_template.json', 'r', encoding='UTF-8') as f:
        DB.update(json.loads(f.read()))
    
    
    if Ver < DB['Version'] :
        logging.info('New version detected. please download newer version in github!')
        logging.info('\n Program will be closed in 5 seconds...')
        sleep(3)
        sys.exit(0)
        
    else:
        pass

    return DB


if __name__ == '__main__':
    DB = dict()
    Ver = 1.0
    download_DB(Ver)
    print(DB) # 테스트
