#-*- coding:utf-8 -*-
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
import json

log = logging.getLogger('RAMS.RWManager')

def askfiledir(titlename, filetype, path=' '):
    ''' finder(titlename, filetype)\n
    titlename : popup title\n
    filetype : input file type, example -> [('name.extension', '*.extension')]\n
    defaultpath : find this file first. if exist, select that. if not, make pop-up window
    '''
    try:
        if os.path.exists(path): #if the file exists.
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

def write_data(path, key, value):
    """add key and value to path file. \n
    path should be a file path. not directory
    """
    if type(path) or type(key) or type(value) != type(str()):
        raise ValueError
        return None
        
    with open(path, mode='r') as f:
        data = json.loads(f.read())
        data[key] = value
    
    with open(path, mode='w') as f:
        f.write(json.dumps(data, indent=4))