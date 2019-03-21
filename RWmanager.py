import logging
import os
import tkinter as tk
import xml.etree.ElementTree as ET
from time import sleep
from tkinter import filedialog
import time
from lxml import etree
import shutil
import time
import os

log = logging.getLogger('RAMS.RWManager')

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

def askfiledir(titlename, filetype, defaultpath=' '):
    ''' finder(titlename, filetype)\n
    titlename : popup title\n
    filetype : input file type, example -> [('name.extension', '*.extension')]\n
    defaultpath : find this file first. if exist, select that. if not, make pop-up window
    '''
    try:
        if os.path.exists(defaultpath): #if the file exists.
            return filedir
        
        else:
            raise ValueError
    
    except:
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

def SaveLOG(_str, _dir, name='RAMSLOG.txt', _mode='a'):
    '''save _str to .txt file, in _dir (_dir should be a folder, not file)\n
name should include file's name and filename extension.\nexample : name=RAMSLOG.txt (default)\n
default mode = 'a'
    '''
    currnetdir = os.getcwd()
    try:
        os.chdir(_dir)
        if type(_str) != type(str()): #if str1 argument isn't a string type.
            return None 

        with open('{}'.format(name), mode=_mode) as f:
            f.write('LOG RECORD TIME : {}'.format(time.strftime("%d %H %M")))
            f.write('---------------')
            f.write(_str)

    except Exception as e:
        log.warning('error while saving LOG to {}, {}'.format(_dir, e))

    os.chdir(currnetdir) # returning to current working tree.

if __name__ == '__main__':
    backup('C:\\Users\\stopc\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Config', 'ModsConfig.xml')