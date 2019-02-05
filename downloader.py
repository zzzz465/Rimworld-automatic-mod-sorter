import json
import os
import shutil
import tempfile
import zipfile
from urllib.request import urlopen

DB_url = 'https://raw.githubusercontent.com/zzzz465/Rimworld-automatic-mod-sorter/master/db_template.json'

def download_DB(DB, Ver): # DB 다운받아서, DB 반환, 버전 체크도 함께
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)
    with urlopen(DB_url) as res:
        res_data = res.read()

        with open('./DB_template.json', 'wb') as f:
            f.write(res_data)
 
    with open('db_template.json', 'r', encoding='UTF-8') as f:
        DB.update(json.loads(f.read()))
    
    
    if Ver < DB['Version'] :
        print('New version detected. please download newer version in github!')
        
    else:
        pass

    return DB


if __name__ == '__main__':
    DB = dict()
    Ver = 1.0
    download_DB(DB,Ver)
    print(DB) # 테스트
