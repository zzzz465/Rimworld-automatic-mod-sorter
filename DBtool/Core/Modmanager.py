import logging
import os
import tkinter
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
import xml.etree.ElementTree as etree
from time import sleep
from lxml import etree

log = logging.getLogger('RAMS.ModManager')
c_steamregpath = "Software\\Valve\\Steam"

HOMEPATH = os.environ['HOMEPATH']
default_cfilepath = HOMEPATH + '\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Config\\ModsConfig.xml'
