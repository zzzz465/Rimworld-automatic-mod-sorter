import sys
import os
from Core import ItemManager, WidgetManager
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1600, 1300)
        self.setMinimumSize(1600, 1800)
        self.setWindowTitle("RAMS dev program")

        #set Root widget and layout setting.
        self.Root_Widget = QtGui.QWidget()
        self.Root_Layout = QtGui.QGridLayout()

        #레이아웃 설정
        self.Root_Widget.setLayout(self.Root_Layout)
        self.setCentralWidget(self.Root_Widget)

        self.mainGUI()

        self.MODListGUI()
        ItemManager.Refesh_list(self.MODlist.ListWidget)

        self.show()

    def mainGUI(self):
        self.RightLayout = QtGui.QVBoxLayout()

        self.Preview = QtGui.QLabel()
        self.RightLayout.addWidget(self.Preview)
        print(self.Preview.size())
        self.PreviewImagePath = os.path.dirname(__file__) + '/Core/no_image.png'
        self.Preview.setPixmap(QtGui.QPixmap(self.PreviewImagePath))
        

        self.Description = QtGui.QTextEdit()
        self.RightLayout.addWidget(self.Description)

        print(self.Description.size())
        self.Preview.setMinimumSize(600,600)
        self.Preview.setMaximumSize(600,600)

        self.Root_Layout.addLayout(self.RightLayout, 0, 1)

    def MODListGUI(self):
        #TODO DB 다운받아오기.
        self.MODlist = WidgetManager.ModList()
        self.MODlist.connect_Info(self.Description, self.Preview)

        self.Root_Layout.addWidget(self.MODlist, 0, 0)
        ItemManager.customWidget.init(self.Description, self.Preview)

        
def main():
    app = QtGui.QApplication(sys.argv)

    GUI = Window()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()