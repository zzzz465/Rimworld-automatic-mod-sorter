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
import mod_sorter
import Parser
import sorter

Version = 0.4 #unstable

HOMEPATH = os.environ['userprofile']
config_folder = r'{}/appdata/locallow/Ludeon Studios/RimWorld by Ludeon Studios/Config'.format(HOMEPATH)


#림월드 폴더 있는지 체크
if os.path.isdir(config_folder):
    pass

else:
    print("can't find rimworld save folder. please install and run Rimworld.") 
    sys.exit(0)

#DB 받아오기
MOD_DB = dict()
downloader.download_DB(MOD_DB, Version)
#print(MOD_DB)

print('Number of MODs registered in DB : {}'.format(len(MOD_DB)))
print('Last DB updated date : {}'.format(MOD_DB['time']))

sleep(1)

ML_workshop = list() #워크샵 모드 리스트
ML_local = list()#로컬 모드 리스트
MD_num_name = dict() # 번호 : 이름
MD_name_num = dict() # 이름 : 번호

rimexedir = str()#림월드 exe 파일 위치
local_mod_dir = str()
workshop_mod_dir = str()

#0. 림월드 위치 묻기
rimexedir, local_mod_dir = finder.finder()

#1. 림월드 로컬 모드 검색
Parser.mod_loader(ML_local, MD_name_num, MD_num_name, local_mod_dir)

#2. 림월드 워크샵 모드 탐색
print(local_mod_dir)
temp = local_mod_dir.split('/')
del temp[4:]
temp = "/".join(temp)
temp = '{}/workshop/content/294100'

Parser.mod_loader(ML_workshop, MD_name_num, MD_num_name, temp)







