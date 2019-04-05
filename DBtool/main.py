import sys
from PyQt4 import QtGui
from Core import WidgetManager, ItemManager

class Window(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("list test")

        #set Root widget and layout setting.
        self.Root_Widget = QtGui.QWidget()
        self.Root_Layout = QtGui.QGridLayout()

        #레이아웃 설정
        self.Root_Widget.setLayout(self.Root_Layout)
        self.setCentralWidget(self.Root_Widget)

        #모드리스트
        #TODO DB 다운받아오기.
        self.MODlist = WidgetManager.ModList()
        self.Root_Layout.addWidget(self.MODlist)

        self.MODlist.ListWidget.addItem

        self.show()

    def doListStuff(self, Modlist):
        
        

def main():
    app = QtGui.QApplication(sys.argv)

    GUI = Window()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()