# https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets

from PyQt4 import QtGui, QtCore
import sys

def setListWidget(widget : QtGui.QListWidget):
    widget.model().rowsInserted.connect()

    def HandleRowInserted(widget, parent, first, last):
        for i in range(first, last+1):
            item = widget.item(i)

            if item != None and widget.itemWidget(i) == None:
                index, name, icon = item.data(QtCore.Qt.UserRole)

                