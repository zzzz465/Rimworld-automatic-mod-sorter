import os
import re
import shutil
import sys
from time import sleep
import re

from colorama import Fore as Color
from colorama import init

import backup
import downloader
import finder
import Parser
import sorter

Version = 0.4 #unstable

init(autoreset=True)

HOMEPATH = os.environ['userprofile']
DESKTOP = '{}/desktop'.format(HOMEPATH)
cfolder = r'{}/appdata/locallow/Ludeon Studios/RimWorld by Ludeon Studios/Config'.format(HOMEPATH)
#디폴트 폴더

#림월드 폴더 있는지 체크
if os.path.isdir(cfolder):
    pass

else:
    print("can't find rimworld config save folder.")
    print('Type 1 to select your config file. type 2 to exit program.')

    breakloop = False
    while breakloop == False:
        x = input('input >> ')        
        if x == '1':
            breakloop = True
            cfolder = finder.finder_folder()

        elif x == '2':
            sys.exit(0)

        else:
            print('wrong input. Please input 1 or 2')


        
#DB 받아오기
MOD_DB = dict()
downloader.download_DB(MOD_DB, Version)
#print(MOD_DB)

print('Number of Mods registered in DB : {}'.format(len(MOD_DB)))
print('Last DB updated date : {}'.format(MOD_DB['time']))

sleep(1)

ML_workshop = list() #워크샵 모드 리스트
ML_local = list()#로컬 모드 리스트
ML_active = list() # 활성화된 모드 리스트
MD_num_name = dict() # 번호 : 이름
MD_name_num = dict() # 이름 : 번호
ML_sorted = list() # 배열이 완료된 리스트
ML_error = list() #배열 안된 리스트

rimexedir = str()#림월드 exe 파일 위치
local_mod_dir = str()
workshop_mod_dir = str()

#0. 림월드 위치 묻기
rimexedir, local_mod_dir = finder.finder()

#1. 림월드 로컬 모드 검색
Parser.mod_loader(ML_local, MD_name_num, MD_num_name, local_mod_dir)

#2. 림월드 워크샵 모드 탐색
workshop_skip = False
try:
    temp = local_mod_dir.split('/')
    del temp[4:]
    temp = "/".join(temp)
    workshop_dir = '{}/workshop/content/294100'.format(temp)
    if os.path.isdir(workshop_dir) == False:
        raise(ValueError)

except:
    print('cannot find workshop folder.')
    print('type Y to select workshop folder, type N to skip workshop mod.')
    breakloop = False
    while breakloop == False:
        x = input('type Y or N : ')
        if x == 'Y':
            workshop_dir = finder.finder_folder()
            breakloop = True
        
        elif x == 'N':
            breakloop = True
            workshop_skip = True

        else:
            print('wrong input. please type Y or N')


if workshop_skip == False:
    Parser.mod_loader(ML_workshop, MD_name_num, MD_num_name, workshop_dir)

else:
    pass

#3. 컨픽 파일 읽어오기
Parser.config_loader(cfolder, ML_active)

#4. 배열하기
ML_sorted, ML_error = sorter.give_num(ML_active, MD_num_name, MD_name_num, MOD_DB)

#5. 컨픽 파일 수정하기
Parser.config_updater(cfolder, ML_sorted)

#6. 리스트 보여주기
Parser.showlist(ML_sorted, ML_workshop, ML_local, MD_num_name)

#7.파일 읽고 쓰기
os.chdir(DESKTOP)
with open('ML_not_in_the_DB.txt', 'w', encoding='UTF-8') as f:
    for x in ML_error:
        f.write(x)
        f.write('\n')


#8. 안내
print('work done!')
print('starting Rimworld...')

os.startfile(rimexedir)
print('Please check this terminal.')

print('program will be closed in 5 seconds...')
sleep(5)
sys.exit(0)



