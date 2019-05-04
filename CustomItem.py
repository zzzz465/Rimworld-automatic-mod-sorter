from PyQt4 import QtGui
from PyQt4 import QtCore

StyleAuthor = '''
QLabel {
    font-size : 12px;
    color : gray;
}'''

StyleName = '''
QLabel {
    font-size : 16px;
}'''

class CustomWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.VBoxLayout = QtGui.QVBoxLayout()
        self.ModName = QtGui.QLabel()
        self.ModName.setFixedWidth(300)
        self.ModAuthor = QtGui.QLabel()

        self.VBoxLayout.addWidget(self.ModName, 0)
        self.VBoxLayout.addWidget(self.ModAuthor, 1)
        self.VBoxLayout.setSpacing(4)
        self.VBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.VBoxLayout.setSpacing(0)
        self.ModAuthor.setStyleSheet(StyleAuthor)
        self.ModName.setStyleSheet(StyleName)

        self.setLayout(self.VBoxLayout)

    def setModName(self, text):
        self.ModName.setText(text)

    def setModAuthor(self, text):
        self.ModAuthor.setText(text)

    def setIcon(self, bool): #TODO 스팀 ->1, 로컬 -> 0
        if bool == True:
            pass
        
        else:
            pass

def setCustomWidgetItem(QWidget : QtGui.QWidget, QListWidget : QtGui.QListWidget, Mod): #리스트에 아이템을(위젯설정하여) 등록
    '''
    Qwidget -> CustomWidget, QListWidget -> CustomListWidget
    '''
    def GetDBValue(DB, name):
        try:
            num = DB[name]
            return num
        
        except:
            return None

    try:
        data = {
            'name' : Mod.name,
            'key' : Mod.key,
            'author' : Mod.author,
            'cver' : Mod.currentVer,
            'description' : Mod.description,
            'Qsize' : QtCore.QSize(20,50),
            'path' : Mod.path
        }
        CustomItem = QtGui.QListWidgetItem(QListWidget)
        CustomItem.setSizeHint(data['Qsize'])

        QListWidget.addItem(CustomItem)
        CustomItem.setData(QtCore.Qt.UserRole, data)
        CustomItem.setData(QtCore.Qt.DisplayRole, GetDBValue(QListWidget.DB, data['name']))

        QListWidget.setItemWidget(CustomItem, QWidget)

    except Exception as e:
        print(e)
        pass

def isActive(activeModList, Mod):
    
    if Mod.key in activeModList:
        return True

    else:
        return False

def LoadItemToList(ModList, AvailableQwidget, ActiveQwidget, activeModList):

    for Mod in ModList:
        item = CustomWidget()
        item.setModName(Mod.name)
        item.setModAuthor(Mod.author)
        #item.setIcon()

        if isActive(activeModList, Mod):
            setCustomWidgetItem(item, ActiveQwidget, Mod)

        else:
            setCustomWidgetItem(item, AvailableQwidget, Mod)