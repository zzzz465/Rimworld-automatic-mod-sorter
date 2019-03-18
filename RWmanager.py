import logging
import os
import tkinter as tk
import xml.etree.ElementTree as ET
from time import sleep
from tkinter import filedialog
import time
from lxml import etree
import shutil

def LoadXML(dir_XMLfile): #  Root를 넘겨줌
    doc = ET.parse(dir_XMLfile)
    root = doc.getroot()

    return root

def LoadActMod(root):
    '''
        accept ET root for argument\n
        return list of mod key
    '''
    ActiveMod = root.find('activeMods')
    active_mod = list()

    for li in ActiveMod.findall('li'):
        active_mod.append(str(li.text))

    return active_mod #Modkey를 반환

def askfiledir(titlename, filetype):
    ''' finder(titlename, filetype)\n
         titlename : 제목 설정\n
         filetype : 리스트 형식을 입력 예시 = [('이름.확장자', '*.확장자')]
    '''
    cdir = os.path.dirname(os.path.realpath(__file__))
    root = tk.Tk()
    filedir = filedialog.askopenfilename(initialdir = cdir, title = titlename, filetype = filetype)
    root.destroy()

    return filedir

def askfolderdir(titlename="select folder."): # 폴더 디렉토리 반환
    root = tk.Tk()
    dir1 = filedialog.askdirectory(initialdir = 'C:/', title = titlename)
    root.destroy()

    return dir1

def backup(dir1, file1):
    '''
        dir1 = 폴더 경로 (os.chdir()  이용)\n
        file = 파일 이름 str 형식
    '''

    currentpath = os.getcwd()
    os.chdir(dir1)
    now_time = time.strftime('%d_%H_%M', time.localtime(time.time()))
    shutil.copy('{}'.format(file1), '{}.backup_{}'.format(file1,now_time))

    logging.info('backup config file created. [{}.backup.{}]'.format(file1,now_time))
    os.chdir(currentpath)



if __name__ == '__main__':
    backup('C:\\Users\\stopc\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Config', 'ModsConfig.xml')


