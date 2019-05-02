# https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets

from PyQt4 import QtGui, QtCore
import sys, CustomItem

def setListWidget(widget : QtGui.QListWidget):
    widget.model().rowsInserted.connect(HandleRowInserted, QtCore.Qt.QueuedConnection)
    widget.setAcceptDrops(True)

    def HandleRowInserted(widget, parent, first, last):
        for i in range(first, last+1):
            item = widget.item(i)

            if item != None and widget.itemWidget(i) == None:
                name, key, author, currentVer, description = item.data(QtCore.Qt.UserRole)
    