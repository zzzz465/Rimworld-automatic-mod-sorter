from PyQt4 import QtGui
import xml.etree.ElementTree as ET
import logging
import os
try:
    from . import RWmanager
except:
    pass

from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER

log = logging.getLogger("RAMS.DevTool.ItemManager")


class customWidget(QtGui.QWidget):
    description = None
    preview = None
    def __init__(self, MODname, MODkey, Author, Relative, ImagePath, description): #TODO 파라매터 하나 추가하고, 경로에 따른 그림 설정하는 기능 추가.
        super(customWidget, self).__init__(None)
        self.MODname = MODname
        self.MODkey = MODkey
        self.Author = Author
        self.Relative = Relative
        self.PreviewImagePath = ImagePath
        self.Description = description
        
        #set layout.
        #큰 프레임(Horizon 프레임),0번째 슬롯은 스팀 또는 로컬 구분용 그림을 넣고, 1번째 프레임에는 이름과 Author가 들어감. 2번째 프레임에는 버튼 기능들이 들어감(아마도)
        self.RootLayout = QtGui.QHBoxLayout()

        self.source_logo = QtGui.QLabel() # will indicate steam, workshop or local mod.
        self.RootLayout.addWidget(self.source_logo, 0)

        #set info Layout. this will include Name, and author
        self.infoLayout = QtGui.QVBoxLayout()
        self.Label_MODname = QtGui.QLabel(self.MODname)
        self.Label_Author = QtGui.QLabel(self.Author)
        self.infoLayout.addWidget(self.Label_MODname)
        self.infoLayout.addWidget(self.Label_Author)
        self.RootLayout.addLayout(self.infoLayout, 1)

        #Order Number를 저장하는 공간
        self.OrderNum = float()
        '''
        self.OrderNum = QtGui.QLineEdit()
        self.RootLayout.addWidget(self.OrderNum)
        self.OrderNum.setDisabled(True)
        self.
        '''

        #this will set Layout for this.
        self.setLayout(self.RootLayout)

    @classmethod
    def init(cls, preview, description):
        cls.description = description
        cls.preview = preview

    def changeInfo(self):
        customWidget.preview.setPixmap(QtGui.QPixmap(self.PreviewImagePath))

    #def refresh(self):

class ModBase:
    DB = dict()
    XMLpath = str() #컨픽파일 경로 저장
    Steampath = str() # steam path or None
    LocalModpath = str()
    WorkshopModpath = str()

    def __init__(self):
        pass

    @staticmethod
    def init(cls, DB, Steampath, LocalModpath, WorkshopModpath):
        cls.DB = DB
        cls.Steampath = Steampath
        cls.LocalModpath = LocalModpath
        cls.WorkshopModpath = WorkshopModpath

class Mod(ModBase):
    def __init__(self, path, name, author, ImagePath, Description):
        self.MODfolderpath = path
        self.MODname = name
        self.MODkey = os.path.basename(self.MODfolderpath)
        self.Author = author
        self.ImagePath = ImagePath
        self.Description = Description

def Get_XMLValue(XMLpath, value):
    '''
    read value from About.xml
    return value
    '''
    try:
        doc = ET.parse(XMLpath)
        root = doc.getroot()
        value = root.find(value).text

        return value

    except Exception as e:
        log.error('Error : {}'.format(e))

def Load_Mod(Modpath):
    ''' load mod in Modpath, return Mod list
    '''
    folder_list = os.listdir(Modpath)

    MODlist = list()
    
    for key in folder_list:
        try:
            abspath = Modpath + "\\{}".format(key)
            XMLpath = abspath + '\\About\\About.xml'
            MODname = Get_XMLValue(XMLpath, 'name')
            MODAuthor = Get_XMLValue(XMLpath, 'author')
            ImagePath = abspath + '\\about\\Preview.png'
            Description = Get_XMLValue(XMLpath, 'description')
            x = Mod(abspath, MODname, MODAuthor, ImagePath, Description)

            MODlist.append(x)

        except:
            log.warning('cannot read mod key : {}'.format(key))
            
    return MODlist

def Add_Mod(MODLIST, QListWidget):
    for x in MODLIST:      
        myQCustomWidget = customWidget(x.MODname, x.MODkey, x.Author, None, x.ImagePath, x.Description) #커스텀 위젯을 만들고.

        myQListWidgetItem = QtGui.QListWidgetItem(QListWidget) #리스트 아이템을 선언해주고, 리스트에 등록
        myQListWidgetItem.setData(20, myQCustomWidget.PreviewImagePath)
        myQListWidgetItem.setData(21, myQCustomWidget.Description)
        myQListWidgetItem.setData(22, myQCustomWidget.OrderNum)
        myQListWidgetItem.setData(23, myQCustomWidget.MODname)

        myQListWidgetItem.setSizeHint(myQCustomWidget.sizeHint()) #사이즈 힌트 알려주고

        QListWidget.addItem(myQListWidgetItem) #아이템을 리스트에 담음
        QListWidget.setItemWidget(myQListWidgetItem, myQCustomWidget) #리스트의 아이템을 나의 커스텀 아이템으로 설정

def Refesh_list(QListWidget):
    list1 = Load_Mod(r'C:\Program Files (x86)\Steam\steamapps\common\RimWorld\Mods1')
    Add_Mod(list1, QListWidget)