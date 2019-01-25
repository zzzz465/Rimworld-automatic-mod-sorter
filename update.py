from urllib.request import urlopen
import os
import zipfile
dir = os.environ['HOMEPATH']
dir = str(dir) + '/desktop'


os.chdir(dir)
os.mkdir('rimworld_mod_sorter')
os.chdir('./rimworld_mod_sorter')


url = 'https://github.com/zzzz465/Rimworld-automatic-mod-sorter/archive/master.zip'


with urlopen(url) as res:
    res_data = res.read()

    with open('./template.zip', 'wb') as f:
        f.write(res_data)

template = zipfile.ZipFile('template.zip')
template.extractall('./')
template.close()

os.chdir('./Rimworld-automatic-mod-sorter-master')
with open('db_template.json', 'r') as f:
    return 