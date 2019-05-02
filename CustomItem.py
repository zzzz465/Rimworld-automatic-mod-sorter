from PyQt4 import QtGui
from PyQt4 import QtCore

class CustomWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.GridLayout = QtGui.QGridLayout()
        self.ModName = QtGui.QLabel()
        self.ModAuthor = QtGui.QLabel()
        self.Icon = QtGui.QLabel()

        self.GridLayout.addWidget(ModName, 0, 0)
        self.GridLayout.addWidget(ModAuthor, 0, 1)
        self.GridLayout.addwidget(Icon, 1, 0)

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

def setCustomWidgetItem(QWidget : QtGui.QWidget, QListWidget : QtGui.QListWidget, Mod):
    '''
    Qwidget -> CustomWidget, QListWidget -> CustomListWidget
    '''
    data = (Mod.name, Mod.author, Mod.currentVer, Mod.description)
    CustomItem = QtGui.QListWidgetItem(QListWidget)
    CustomItem.setSizeHint(QWidget.sizeHint())
    
    QListWidget.addItem(CustomItem)
    CustomItem.setData(QtCore.Qt.UserRole, data)

    QListWidget.setItemWidget(CustomItem, QWidget)