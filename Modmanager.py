import logging
import os
import tkinter as tkinter
import xml.etree.ElementTree as ET
import logging
from time import sleep

from lxml import etree

import RWmanager
import downloader

log = logging.getLogger('RAMS.ModManager')

class ModBase:
    DB = dict()#DB저장
    ActiveModlist = list()#modkey 저장(활성화)
    ConfigXmldir = str() #컨픽파일 경로 저장
    ConfigXmlfolderdir = str()

    @classmethod
    def setDB(cls, DB):
        cls.DB = DB 

    @classmethod
    def setXmldir(cls, dir1):
        cls.ConfigXmldir = dir1
        cls.ConfigXmlfolderdir = dir1[:len(cls.ConfigXmldir) - 15]
    
    def __init__(self):
        if ModBase.DB == {}:
            ModBase.setDB(ModBase.DB)

        #if ModBase.ConfigXmldir == str():
        #    ModBase.ConfigXmldir = RWmanager.askfiledir('select Rimworld config file.', [('ModsConfig.xml', '*.*')])
    
        #if ModBase.ConfigXmldir

        if ModBase.ActiveModlist == []:
            root = RWmanager.LoadXML(ModBase.ConfigXmldir)
            ModBase.ActiveModlist = RWmanager.LoadActMod(root)
            sleep(2)
            log.info('Active mod list loaded.')
            sleep(1)
            log.info('current active mod number > {}'.format(len(ModBase.ActiveModlist)))
            


class Mod(ModBase):
    Modcount = 0
    MODs = list() # every mod data will saved in this list
    list1 = list() # deactivated
    list2 = list() # activated but removed cuz not on the activelist
    list3 = list() # activated and will load on activelist

    def __init__(self, moddir, modkey):    
        super().__init__()
        self.MODkey = str(modkey)
        self.MODdir = str(moddir) # folder location
        self.dir_Aboutxml = '{}/About/About.xml'.format(self.MODdir)
        self.MODname = parseXML(self.dir_Aboutxml, 'name')
        self.OrderNum = self.SetOrderNum()

    @classmethod
    def Modcountplus(cls):
        cls.Modcount += 1

    @staticmethod
    def getOrderNum(self):
        return self.OrderNum

    @classmethod
    def Sort(cls): # 항상 마지막에 호출
        for x in cls.MODs:
            if x.MODkey in cls.ActiveModlist: # if the mod is on the list
                
                if x.OrderNum != None: # and if the mod is in the DB
                    cls.list3.append(x)

                else:
                    cls.list2.append(x)
            
            else:
                cls.list1.append(x)

        cls.list3.sort(key=Mod.getOrderNum)

                    

    
    def SetOrderNum(self):
        sleep(0.08)
        if self.MODname in Mod.DB:
            num = Mod.DB[self.MODname]
            log.info("grant mod number {} to mod name > {}".format(num, self.MODname))
            return float(num)

        else:
            log.warning('ERROR while giving order number to mod > {}'.format(self.MODname))
            return None

class ModWorkshop(Mod):
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)

class ModLocal(Mod):
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)

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
    
def LoadMod(dir1, type1='Local'):
    '''
        dir = 모드 폴더 경로\n
        type = 'Local' 또는 'Workshop'
    '''
    log.debug('LoadMod 호출')
    folderlist = os.listdir(dir1)
    log.debug('dir1 폴더에서 폴더 {} 개를 찾았습니다.'.format(len(folderlist)))
    log.debug(dir1)
    if type1 == 'Local':
        list1 = list()
        for folder in folderlist:
            try:
                log.debug('폴더 {}'.format(folder))
                dir2 = dir1 + '/{}'.format(folder)
                list1.append(ModLocal(dir2, folder))
                log.debug(folder + ' ' + dir2)

            except Exception as e:
                log.warning('cannot read About.xml in mod number > {}'.format(folder))
                log.debug('에러 코드 : {}'.format(e))
        Mod.MODs = Mod.MODs + list1

    else:
        list1 = list()
        for folder in folderlist:
            try:
                log.debug('폴더 {}'.format(folder))
                dir2 = dir1 + '/{}'.format(folder)
                list1.append(ModWorkshop(dir2, folder))
                log.debug('{} {}'.format(dir2, folder))

            except Exception as e:
                log.debug('LoadMod workshop 돌던 중 에러 발생')
                log.debug('에러 코드 : {}'.format(e))
        Mod.MODs = Mod.MODs + list1

def update_config(dir1, mod):
    currentdir = os.getcwd()
    os.chdir(dir1)

    
    list1 = list()
    for x in mod:
        try:
            list1.append(str(x.MODkey))
            log.info('Record Mod > {}'.format(str(x.MODname)))
            sleep(0.1)

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
    sleep(2)
    root.remove(root.find('activeMods')) # remove activemods tag and below
    ActiveMods = ET.SubElement(root, 'activeMods') # make a tag
    
    log.info('overriding mod lists...')
    for x in Mods:
        mod = ET.SubElement(ActiveMods, 'li')
        mod.text = str(x)

    sleep(3)    
    doc.write('ModsConfig.xml', encoding='UTF-8', xml_declaration='False')
    log.info('ModsConfig.xml saved...')


if __name__ == '__main__': # for testing

    
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    x = RWmanager.askfolderdir()
    DB = downloader.download_DB(0.5)
    ModBase.setDB(DB)
    LoadMod(x, 'Workshop')
    print(len(Mod.MODs))
    