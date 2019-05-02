# https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets

from PyQt4 import QtGui, QtCore
import sys, types, CustomItem, inspect

#https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance

def setListWidget(widget : QtGui.QListWidget):
    widget.model().rowsInserted.connect(lambda x, first, last : HandleRowInserted(widget, first, last), QtCore.Qt.QueuedConnection)
    #widget.actionEvent()
    widget.setAcceptDrops(True)
    widget.setDragEnabled(True)
    widget.setDragDropMode(3) #set to DragDrop

def HandleRowInserted(widget, first, last):
    for i in range(first, last+1):
        item = widget.Item(i)

        if item != None and widget.itemWidget(item) == None:
            name, key, author, currentVer, description = item.data(QtCore.Qt.UserRole)
            
            thisItem = CustomItem.CustomWidget()
            thisItem.setModName(name)
            thisItem.setModAuthor(author)
            item.setSizeHint(thisItem.sizeHint())
            widget.setItemWidget(item, thisItem)


#def HandleDragEnterEvent(self, ):
#    print(args)

    