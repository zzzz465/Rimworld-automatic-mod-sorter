import json
import os

import downloader


def return_local_db():
    os.chdir(os.environ['HOMEPATH'])
    os.chdir('./desktop')

    local_dic = dict()
    with open('db_template.json', 'r', encoding='UTF-8') as f:
        temp = json.loads(f.read())
        local_dic.update(temp)
    return local_dic

def return_compare_dic():
    local_db = return_local_db()
    data = downloader.update() #최신 DB를 받아옴.
    added_dic = dict()
    
    for x in local_db: #추가된 것만 골라서 받아옴
        if x in data:
            continue
        
        else:
            added_dic[x] = local_db[x]
    return added_dic


if __name__ == '__main__':
    return_compare_dic()
