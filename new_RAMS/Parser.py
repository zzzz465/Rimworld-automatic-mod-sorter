import os
import tkinter as tkinter
import xml.etree.ElementTree as ET
from tkinter import filedialog

from lxml import etree

HOMEPATH = os.environ['userprofile']
rimsavedir = r'{}/appdata/locallow/Ludeon Studios/RimWorld by Ludeon Studios/Config'.format(HOMEPATH)


def mod_loader(mod_list, MFD, MFDN, dir):#모드 리스트, 모드이름(키) : 폴더이름(값), 폴더이름 : 모드이름, 경로 받아옴
    os.chdir(dir)
    folder_list = os.listdir(dir)

    for x in folder_list:
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


def config_loader(cfdir, active_mod): #컨픽파일 모드 리스트 가져오기
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()
    ActiveMod = root.find('activeMods')

    for li in ActiveMod.findall('li'):
        active_mod.append(str(li.text))


    










if __name__ == '__main__':
    pass