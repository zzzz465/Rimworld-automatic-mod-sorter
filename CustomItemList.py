# https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets

from PyQt4 import QtGui, QtCore
import sys, types, CustomItem, os

#https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance

StyleList = '''
    QListWidget {
        
        }
    QScrollBar:vertical {
        width : 16px;
        }'''

class ModListWidget(QtGui.QListWidget):
    def __init__(self, info, DB):
        super().__init__()
        self.DB = DB
        self.setAcceptDrops(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setAutoScroll(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setStyleSheet(StyleList)
        self.setSpacing(2)
        self.InfoData = info
        self.setAutoScroll(True)
        
        self.setConnection()
    
    def setConnection(self):
        self.model().rowsInserted.connect(self.HandleRowInserted, QtCore.Qt.QueuedConnection)
        self.currentItemChanged.connect(self.SelectedHandle)


    def HandleRowInserted(self, parent, first, last):
        for index in range(first, last + 1):
            item = self.item(index)
            if item != None and self.itemWidget(item) == None:
                ItemData = item.data(QtCore.Qt.UserRole)
                ThisWidget = CustomItem.CustomWidget()
                ThisWidget.setModName(ItemData['name'])
                ThisWidget.setModAuthor(ItemData['author'])
                #ThisWidget.setIcon()
                item.setSizeHint(ItemData['Qsize'])
                self.setItemWidget(item, ThisWidget)
    
    def SelectedHandle(self, CurrentItem : QtGui.QListWidgetItem, previousItem):
        Itemdata = CurrentItem.data(QtCore.Qt.UserRole)
        self.InfoData['TitleLabel'].setText(Itemdata['name'])
        self.InfoData['AuthorLabel'].setText(Itemdata['author'])
        self.InfoData['CVerLabel'].setText(Itemdata['cver'])
        SortNum = str(CurrentItem.data(QtCore.Qt.DisplayRole))
        if SortNum == '':
            SortNum = 'None'
        self.InfoData['SortNumLabel'].setText(SortNum)
        
        self.setPreviewImage()

    def setPreviewImage(self):
        itemData = self.currentItem().data(QtCore.Qt.UserRole)
        ImageBrowser = self.InfoData['ImageBrowser']
        path = itemData['path']
        PreviewImagePath = '\\'.join([path, 'About', 'Preview.png'])
        
        if os.path.isfile(PreviewImagePath):
            QPixmap = QtGui.QPixmap(PreviewImagePath)
            ImageBrowser.setPixmap(QPixmap)

        else:
            QPixmap = QtGui.QPixmap(self.InfoData['defaultImagePath'])
            ImageBrowser.setPixmap(QPixmap)



    