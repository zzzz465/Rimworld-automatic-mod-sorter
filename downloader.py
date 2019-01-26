from urllib.request import urlopen
import os
import zipfile
import json
import shutil
import tempfile
def update():
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)
    url = 'https://github.com/zzzz465/Rimworld-automatic-mod-sorter/archive/master.zip'
    with urlopen(url) as res:
        res_data = res.read()

        with open('./template.zip', 'wb') as f:
            f.write(res_data)

    template = zipfile.ZipFile('template.zip')
    template.extractall('./')
    template.close()

    os.chdir('./Rimworld-automatic-mod-sorter-master')

    f = open('db_template.json', 'r')
    return_dict = json.loads(f.read())
    f.close()
    
    #print(return_dict)
    return return_dict #return_dict로 다운받은 최신 dictionary를 받아옴



if __name__ == '__main__':
    pass