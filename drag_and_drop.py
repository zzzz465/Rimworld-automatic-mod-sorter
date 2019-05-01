import sys, os
from PyQt4 import QtGui, QtCore

class ThumbListWidget(QtGui.QListWidget):
    def __init__(self, type, parent=None): #드래그 앤 드랍을 받을 리스트
        super(ThumbListWidget, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)#드래그드랍허용
        self.model().rowsInserted.connect(
            self.handleRowsInserted, QtCore.Qt.QueuedConnection) #rowInserted(parent, first, last)를 갖는데, 이것이 connect 내의 self.handlerowsinserted으로 넘겨짐

    def handleRowsInserted(self, parent, first, last):
        for index in range(first, last + 1):
            item = self.item(index)
            if item is not None and self.itemWidget(item) is None: #item는 비어있는 아이템 체크, itemwidget는 아이템이 있어도, 내부 위젯이 있는지 없는지 검사
                index, name, icon = item.data(QtCore.Qt.UserRole) #UserRole이라는 곳에서 Data를 읽어옴(아마도 튜플 형식?)
                #리스트 아이템 construct 하는곳. 함수로 만들어서 넘겨주는게 좋을듯?
                widget = QCustomQWidget() #밑에있는 construct
                widget.setTextUp(index)
                widget.setTextDown(name)
                widget.setIcon(icon)
                item.setSizeHint(widget.sizeHint())
                self.setItemWidget(item, widget)

class Dialog_01(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow,self).__init__()
        self.listItems = {}

        myQWidget = QtGui.QWidget()
        myBoxLayout = QtGui.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.myQListWidget = ThumbListWidget(self)

        myBoxLayout.addWidget(self.myQListWidget)

        for data in [
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            myQListWidgetItem = QtGui.QListWidgetItem(self.myQListWidget)
            # store the data needed to create/re-create the custom widget
            myQListWidgetItem.setData(QtCore.Qt.UserRole, data)
            self.myQListWidget.addItem(myQListWidgetItem)

        self.listWidgetB = ThumbListWidget(self)
        myBoxLayout.addWidget(self.listWidgetB)

class QCustomQWidget (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtGui.QVBoxLayout()
        self.textUpQLabel    = QtGui.QLabel()
        self.textDownQLabel  = QtGui.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtGui.QHBoxLayout()
        self.iconQLabel      = QtGui.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    dialog_1 = Dialog_01()
    dialog_1.show()
    dialog_1.resize(480,320)
    app.exec_()