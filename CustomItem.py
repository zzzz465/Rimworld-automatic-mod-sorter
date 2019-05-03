from PyQt4 import QtGui
from PyQt4 import QtCore

StyleAuthor = '''
QLabel {
    font-size : 20px;
    color : gray;
}'''

StyleName = '''
QLabel {
    font-size : 30px;
}'''

class CustomWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.VBoxLayout = QtGui.QVBoxLayout()
        self.ModName = QtGui.QLabel()
        self.ModAuthor = QtGui.QLabel()

        self.VBoxLayout.addWidget(self.ModName, 0)
        self.VBoxLayout.addWidget(self.ModAuthor, 1)
        self.VBoxLayout.setSpacing(4)


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
    try:
        data = (Mod.name, Mod.key, Mod.author, Mod.currentVer, Mod.description, QtCore.QSize(20, 85))
        CustomItem = QtGui.QListWidgetItem(QListWidget)
        CustomItem.setSizeHint(data[len(data) - 1])

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