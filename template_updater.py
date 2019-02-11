import downloader
import finder
import mod_sorter
import Parser
import sorter
from time import sleep
import re

import os
import re
import shutil
import sys
import toolbox

from colorama import Fore as Color
from colorama import init

init(autoreset=True)

ML_Local = list()
MD_name_num = dict()
MD_num_name = dict()
MD_list = list()
ML_workshop = list()

rimexedir = str()
local_mod_dir = str()
workshop_mod_dir = str()

#0. DB 다운로드 받기
MOD_DB = dict()
Ver = 1.0
downloader.download_DB(MOD_DB, Ver)


#0. 림월드 위치 묻기
rimexedir, local_mod_dir = finder.finder()
print('\n')

#1. 림월드 로컬 모드 검색
Parser.mod_loader(ML_Local, MD_name_num, MD_num_name, local_mod_dir)
print('\n')

#2. 림월드 워크샵 모드 탐색
workshop_skip = False
try:
    temp = local_mod_dir.split("/")
    del temp[len(temp) - 3:]
    temp = "\\".join(temp)
    workshop_dir = '{}\\workshop\\content\\294100'.format(temp)
    if os.path.isdir(workshop_dir) == False:
        raise(ValueError)

except:
    print('cannot find workshop folder.')
    print('type Y to select workshop folder, type N to skip workshop mod.')
    breakloop = False
    while breakloop == False:
        x = input('type Y or N : ')
        
        if x.isalnum():
            x = x.lower()
            if x == 'y':
                workshop_dir = finder.finder_folder()
                workshop_dir = '{}/content/294100'.format(workshop_dir)
                breakloop = True
        
            elif x == 'n':
                breakloop = True
                workshop_skip = True

        else:
            print('wrong input. please type Y or N')

if workshop_skip == False:
    Parser.mod_loader(ML_workshop, MD_name_num, MD_num_name, workshop_dir)
print('\n')

#3. 중복되는 모드 제거
MD_list = ML_Local + ML_workshop

MD_list = toolbox.overlap_remover(MOD_DB, MD_list) # 중복 제거된 리스트 가져오기



#4. 배열하기
DB_new = dict()
print('Current mod number registered in DB : ' + Color.LIGHTGREEN_EX + str(len(MOD_DB) -1))
print('last DB updated time : ' + Color.LIGHTMAGENTA_EX + str(MOD_DB['time']))
print('\n')
if len(MD_list) > 0:
    print('New mod detected.')
    print('Are you want to add mods to the DB?')

    breakloop = False
    while breakloop == False:
        _input = input('Y or X : ')

        if _input.isalpha():
            if _input.lower() == 'y':
                DB_new = toolbox.mod_update(MD_list)
                breakloop = True

            elif _input.lower() == 'x':
                breakloop = True
                print('exit program..')
                sys.exit(0)

        else:
            print('wrong input.')

if len(MD_list) == 0:
    print('already all mods are registered in DB.')
    print('exit program...')
    sys.exit(0)

#5. DB 업데이트
toolbox.DB_update(MOD_DB, DB_new)

#6. DB 저장
toolbox.DB_save(MOD_DB)

print('Work done!')
print('exit program...')






        
            










