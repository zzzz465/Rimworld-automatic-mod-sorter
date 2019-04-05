#-*- coding:utf-8 -*-
import logging
import os
import tkinter as tkinter
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER  # for steam folder location.
import xml.etree.ElementTree as ET
from time import sleep
from lxml import etree

try:
    from . import RWmanager

except:
    pass

log = logging.getLogger('RAMS.ModManager')
c_steamregpath = "Software\\Valve\\Steam"

HOMEPATH = os.environ['HOMEPATH']
default_cfilepath = HOMEPATH + '\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Config\\ModsConfig.xml'

def parseXML(dir_XML, attribute):
    if type(dir_XML) != type(str()):
        log.error('cannot read XML file directory. ')
        log.debug(str(dir_XML), ' - dir_XML 내용')
        return None
    
    if type(attribute) != type(str()):
        log.error('wrong attribute data type.')
        log.debug(str(attribute))
        return None

    try:
        doc = ET.parse(dir_XML)
        root = doc.getroot()
        name = root.find(attribute).text
        log.debug('{}에서 {}를 찾았습니다.'.format(dir_XML, attribute))
        return name

    except Exception as e:
        log.debug('parseXML에서 에러 발생')
        log.debug(e)
    
def LoadMod(dir1, type1=1):
    '''
        dir = 모드 폴더 경로\n
        type
        1 = Local
        2 = Workshop
        
    '''
    if dir1 == None:
        return None
        
    folderlist = os.listdir(dir1)
    log.debug('dir1 폴더에서 폴더 {} 개를 찾았습니다.'.format(len(folderlist)))

    list1 = list()
    for folder in folderlist:
        try:
            log.debug('폴더 {}'.format(folder))
            dir2 = dir1 + '/{}'.format(folder) # Mods folder path
            
            if type1 == 1:
                list1.append(ModLocal(dir2, folder))

            elif type1 == 2:
                list1.append(ModWorkshop(dir2, folder))

        except Exception as e:
            log.warning('cannot read About.xml in mod number > {}'.format(folder))
            log.debug('에러 코드 : {}'.format(e))

    Mod.MODs = Mod.MODs + list1

def update_config(dir1, mod):
    currentdir = os.getcwd()
    os.chdir(dir1)

    
    list1 = list()
    for x in mod:
        try:
            list1.append(str(x.MODkey))

        except Exception as e:
            log.warning('Error while loading Mod {} to order list.'.format(x.MODname))
            log.debug('에러 코드 > {}'.format(e))

    config_updater(dir1, list1)

    os.chdir(currentdir)

def config_loader(cfdir, active_mod): #get a mod list from config file
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()
    ActiveMod = root.find('activeMods')

    for li in ActiveMod.findall('li'):
        active_mod.append(str(li.text))


def config_updater(cfdir, Mods):
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()

    log.info('initializing config file...')
    root.remove(root.find('activeMods')) # remove activemods tag and below
    ActiveMods = ET.SubElement(root, 'activeMods') # make a tag
    
    log.info('overriding mod lists...')
    for x in Mods:
        mod = ET.SubElement(ActiveMods, 'li')
        mod.text = str(x)
 
    doc.write('ModsConfig.xml', encoding='UTF-8', xml_declaration='False')
    log.info('ModsConfig.xml saved...')

def getSteampath():
    '''
    return steam folder dir as string type via registery data
    return None if can't find right value.
    '''
    log.debug('call getSteampath')
    try:
        steamreg = OpenKey(HKEY_CURRENT_USER, c_steamregpath)
        log.debug('steamreg = ' + str(steamreg))
        try:
            value = QueryValueEx(steamreg, "SteamPath")
            log.debug('value : ' + str(value))
            return value[0]
        
        except:
            log.debug('return None')
            return None
    
    except:
        log.debug('return None')
        return None

class ModBase:
    DB = dict()#DB저장
    ActiveModlist = list() # modkey 저장(활성화)
    ConfigXmlpath = str() #컨픽파일 경로 저장
    Configxmlfolderpath = str()
    Steampath = str() # steam path or None
    LocalModpath = str()
    WorkshopModpath = str()

    @classmethod
    def setDB(cls, DB):
        cls.DB = DB 

    @staticmethod
    def setXmlpath():#call in Modbase.__init__()
        if os.path.isfile(default_cfilepath):
            path = default_cfilepath
        
        else:
            path = RWmanager.askfiledir("select ModsConfig.xml", [('ModsConfig.Xml', '*.*')])

        ModBase.ConfigXmlpath = path
        ModBase.Configxmlfolderpath = os.path.dirname(path)

        log.debug('XML path : {} | XML folder path : {}'.format(path, os.path.dirname(path)))

    @classmethod
    def setLocalPath(cls):
        defaultpath = cls.Steampath + '\\steamapps\\common\\RimWorld\\Mods'
        if os.path.isdir(defaultpath):
            cls.LocalModpath = defaultpath

        else:
            cls.LocalModpath = RWmanager.askfolderdir(titlename="select Local Mods folder.")
        
        log.info('Local mod path "{}"'.format(cls.LocalModpath))

    @classmethod
    def setWorkshopPath(cls):
        defaultpath = cls.Steampath + '\\steamapps\\workshop\\content\\294100'
        if os.path.isdir(defaultpath):
            cls.WorkshopModpath = defaultpath

        else:
            if str(input('Load Workshop Mod? Y/N > ')).lower() == 'y':
                logging.info('select your workshop mod folder. folder number is 294100')
                cls.WorkshopModpath = RWmanager.askfolderdir(titlename='Select Workshop 294100 folder')
            
            else:
                return None
                
        log.info('Workshop mod path "{}"'.format(cls.WorkshopModpath))

    @staticmethod
    def setinit(): #TODO merge DB setting and this
        '''
        Always run first before sorting.\n
        find activate mod list, set local/workshop path.
        '''
        ModBase.setXmlpath()
        root = RWmanager.LoadXML(ModBase.ConfigXmlpath)
        ModBase.ActiveModlist = RWmanager.LoadActMod(root)
        log.info('Active mod list loaded.')
        log.info('current active mod number = {}'.format(len(ModBase.ActiveModlist)))

        ModBase.Steampath = getSteampath()
        ModBase.setLocalPath()
        ModBase.setWorkshopPath()

        LoadMod(ModBase.LocalModpath, 1)
        LoadMod(ModBase.WorkshopModpath, 2)

    def __init__(self):
        pass

class Mod(ModBase):
    Modcount = 0
    MODs = list() # every mod data will saved in this list
    list1 = list() # deactivated
    list2 = list() # activated but removed cuz not on the DB
    list3 = list() # activated and will load on activelist
    list4 = list() # deactivated and not on the DB

    def __init__(self, moddir, modkey):
        self.MODkey = str(modkey)
        self.MODdir = str(moddir) # folder location
        self.dir_Aboutxml = '{}/About/About.xml'.format(self.MODdir)
        self.MODname = parseXML(self.dir_Aboutxml, 'name')
        self.OrderNum = self.SetOrderNum()

    @staticmethod
    def getOrderNum(self):
        return self.OrderNum

    @classmethod
    def Sort(cls): # 항상 마지막에 호출
        for x in cls.MODs:
            if x.OrderNum != None: #if it have order number
                if x.MODkey in cls.ActiveModlist:#check to load or not
                    cls.list3.append(x) #load it
                
                else:
                    cls.list1.append(x) #don't load

            else:#if it doesn't have order number
                if x.MODkey in cls.ActiveModlist:#if it activated
                    cls.list2.append(x)

                else:#if it deactivated
                    cls.list4.append(x)

        cls.list3.sort(key=Mod.getOrderNum)

    def SetOrderNum(self):
        if self.MODname in Mod.DB:
            num = Mod.DB[self.MODname]
            log.debug("grant mod number {} to mod name > {}".format(num, self.MODname))
            return float(num)

        else:
            log.debug('ERROR while giving order number to mod > {}'.format(self.MODname))
            return None

class ModWorkshop(Mod): #placeholder
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)

class ModLocal(Mod):
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)
        
if __name__ == '__main__': # for testing
    pass
