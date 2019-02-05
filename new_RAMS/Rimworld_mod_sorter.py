import os
import re
import shutil
import sys
import time
from time import sleep

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

print('Number of MODs registered in DB : {}'.format(len(MOD_DB))
print('Last DB updated date : {}'.format(MOD_DB['time']))

sleep(1)

mod_list_workshop = list()#워크샵 모드 리스트
mod_list_local = list()#로컬 모드 리스트
mod_dic = dict() # 번호 : 이름
mod_dic_num = dict() # 이름 : 번호

rimexedir = str()#림월드 exe 파일 위치
local_mod_dir = str()

#0. 림월드 위치 묻기
rimexedir, local_mod_dir = finder.finder()

#1. 림월드 로컬 모드 검색
Parser.mod_loader()



