from PyQt4 import QtGui
from PyQt4 import QtCore

class CustomWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.GridLayout = QtGui.QGridLayout()
        self.ModName = QtGui.QLabel()
        self.ModAuthor = QtGui.QLabel()
        self.Icon = QtGui.QLabel('IconPH')

        self.GridLayout.addWidget(self.ModName, 0, 0)
        self.GridLayout.addWidget(self.ModAuthor, 1, 0)
        self.GridLayout.addWidget(self.Icon, 0, 1)

        self.setLayout(self.GridLayout)

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
    try:
        data = (Mod.name, Mod.key, Mod.author, Mod.currentVer, Mod.description)
        CustomItem = QtGui.QListWidgetItem(QListWidget)
        CustomItem.setSizeHint(QWidget.sizeHint())

        QListWidget.addItem(CustomItem)
        CustomItem.setData(QtCore.Qt.UserRole, data)

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