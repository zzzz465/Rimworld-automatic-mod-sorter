import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog, QApplication

LocalPath = str()
WorkshopPath = str()
ConfigPath = str()

class AskWindow(QtGui.QWidget):
    global LocalPath
    global WorkshopPath
    global ConfigPath

    def __init__(self, Main):
        super().__init__()
        uic.loadUi("askDialog.ui", self)

        self.Main = Main

        self.setConnection()

    def setConnection(self):
        self.LocalBtn.clicked.connect(lambda x : self.askfolderpath(self.LocalLine))
        self.WorkshopBtn.clicked.connect(lambda x : self.askfolderpath(self.WorkshopLine))
        self.CfgPathBtn.clicked.connect(lambda x : self.askfolderpath(self.CfgLine))

        self.Quit.pressed.connect(self.exit)
        self.OK.pressed.connect(self.okfunc)

    def askfolderpath(self, Line):
        Line.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    def exit(self):
        sys.exit(0)

    def okfunc(self):
        LocalPath = self.LocalLine.text()
        WorkshopLine = self.WorkshopLine.text()
        ConfigPath = self.CfgLine.text()
        self.close()

        self.Main.show()
    
class MainWindow(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('RAMS.ui', self)

        #self.setinit()

    def setinit(self):

    def setConnection(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainscreen = MainWindow()

    askscreen = AskWindow(mainscreen)
    askscreen.show()

    exit(app.exec_())