# https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets

from PyQt4 import QtGui, QtCore
import sys, types, CustomItem, inspect

#https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance

class ModListWidget(QtGui.QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setAutoScroll(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.model().rowsInserted.connect(self.HandleRowInserted, QtCore.Qt.QueuedConnection)

    def HandleRowInserted(self, parent, first, last):
        for index in range(first, last + 1):
            item = self.item(index)
            if item != None and self.itemWidget(item) == None:
                name, key, author, currentVer, description = item.data(QtCore.Qt.UserRole)
                ThisWidget = CustomItem.CustomWidget()
                ThisWidget.setModName(name)
                ThisWidget.setModAuthor(author)
                #ThisWidget.setIcon()
                item.setSizeHint(ThisWidget.sizeHint())
                self.setItemWidget(item, ThisWidget)


    