from PyQt4 import QtGui
import xml.etree.ElementTree as ET
import logging
import os

log = logging.getLogger("RAMS.DevTool.ItemManager")


class customItem(QtGui.QWidget):
    '''
    Dev tool의 리스트에 들어갈 아이템 클래스
    '''

    def __init__(self, MODname, MODkey, Author, Relative): #TODO 파라매터 하나 추가하고, 경로에 따른 그림 설정하는 기능 추가.
        super().__init__()
        self.MODname = MODname
        self.MODkey = MODkey
        self.Author = Author
        self.Relative = Relative
        
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

        #this will set Layout for this.
        self.setLayout(self.RootLayout)

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
    def __init__(self, path, name):
        self.MODfolderpath = path
        self.MODname = name
        self.MODkey = os.path.basename(self.MODfolderpath)
        self.OrderNum = None
        
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

def Load_Mod(Localpath):
    folder_list = os.listdir(Localpath)
    
    for key in folder_list:
        abspath = Localpath + "\\{}".format(key)
        XMLpath = abspath + '\\About\\About.xml'
        MODname = Get_XMLValue(XMLpath, 'name')
        MODk
