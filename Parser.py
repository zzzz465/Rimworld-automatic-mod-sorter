import os
import tkinter as tkinter
import xml.etree.ElementTree as ET
from tkinter import filedialog
from colorama import Fore as Color
from colorama import init
from time import sleep

from lxml import etree

import finder

HOMEPATH = os.environ['userprofile']
rimsavedir = r'{}/appdata/locallow/Ludeon Studios/RimWorld by Ludeon Studios/Config'.format(HOMEPATH)

init(autoreset=True)

def mod_loader(mod_list, MFD, MFDN, dir):#모드 리스트, 모드이름(키) : 폴더이름(값), 폴더이름 : 모드이름, 경로 받아옴
    if os.path.isdir(dir):
        os.chdir(dir)
        folder_list = os.listdir(dir)

        for x in folder_list:
            try:
                os.chdir('{}/{}/About'.format(dir, x))# 각 모드의 About 폴더로 이동

                if os.path.isfile('About.xml'): #파일이 정상적인지 확인
                    pass
                else:
                    continue

                doc = ET.parse('About.xml')
                root = doc.getroot()
                name = root.find('name').text # 모드 이름
                mod_list.append(name)
                
                MFD[name] = x 
                MFDN[x] = name
            
            except:
                pass

    else:
        print("can't find folder.")



def config_loader(cfdir, active_mod): #컨픽파일 모드 리스트 가져오기
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()
    ActiveMod = root.find('activeMods')

    for li in ActiveMod.findall('li'):
        active_mod.append(str(li.text))


def config_updater(cfdir, ML_sorted):
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()

    activeMod = root.find('activeMods')
    print('initializing config file...')

    for li in activeMod.findall('li'):
        activeMod.remove(li)

    sorted_mod = ET.SubElement(activeMod, 'li')
    for x in ML_sorted:
        sorted_mod = ET.SubElement(activeMod, 'li')
        sorted_mod.text = str(x[0][1])

    doc.write('ModsConfig.xml', encoding='UTF-8', xml_declaration='False')


def showlist(ML_sorted, ML_workshop, ML_local, MFDN):
    for x in ML_sorted:
        MOD_name = MFDN[x[0][1]]

        if MOD_name in ML_local:
            print(Color.LIGHTYELLOW_EX + MOD_name)

        elif MOD_name in ML_workshop:
            print(Color.LIGHTGREEN_EX + MOD_name)

        else:
            print(MOD_name)
        sleep(0.1)

if __name__ == '__main__':
    pass