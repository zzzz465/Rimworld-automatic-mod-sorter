from PyQt5 import QtGui, QtCore, QtWidgets

StyleAuthor = '''
QLabel {
    font-size : 12px;
    color : gray;
}'''

StyleName = '''
QLabel {
    font-size : 16px;
}'''

class CustomWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.VBoxLayout = QtWidgets.QVBoxLayout()
        self.VBoxLayout.setSpacing(1)
        self.VBoxLayout.setContentsMargins(2, 0, 0, 2)
        #self.VBoxLayout.setSizeConstraint()
        self.ModName = QtWidgets.QLabel()
        self.ModName.setContentsMargins(0,0,0,0)
        self.ModName.setFixedWidth(300)
        self.ModAuthor = QtWidgets.QLabel()
        self.ModAuthor.setContentsMargins(0,0,0,0)

        self.VBoxLayout.addWidget(self.ModName, 0)
        self.VBoxLayout.addWidget(self.ModAuthor, 1)
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

def setCustomWidgetItem(QWidget : QtWidgets.QWidget, QListWidget : QtWidgets.QListWidget, Mod, kargs={}): #리스트에 아이템을(위젯설정하여) 등록
    '''
    Qwidget -> CustomWidget, QListWidget -> CustomListWidget
    '''

    try:
        data = {
            'name' : Mod.name,
            'key' : Mod.key,
            'author' : Mod.author,
            'cver' : Mod.currentVer,
            'description' : Mod.description,
            'Qsize' : QtCore.QSize(20,40),
            'path' : Mod.path
        }
        data = {**data, **kargs}

        CustomItem = QtWidgets.QListWidgetItem(QListWidget)
        CustomItem.setSizeHint(data['Qsize'])

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

####################

def CCLoadItemToList(Mod, ActiveQwidget, ConflictDescription):
    item = CustomWidget()
    item.setModName(Mod.name)
    item.setModAuthor(Mod.author)
    #item.setIcon()
    
    setCustomWidgetItem(item, ActiveQwidget, Mod, {'ConfData' : ConflictDescription})