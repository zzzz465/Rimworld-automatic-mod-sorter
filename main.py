import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog, QApplication

import ModManager, CustomItem
WorkshopPath = str()
LocalPath = str()
ConfigPath = str()

class AskWindow(QtGui.QWidget):
    global WorkshopPath, LocalPath, ConfigPath

    def __init__(self):
        super().__init__()
        uic.loadUi("askDialog.ui", self)

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
        global LocalPath, WorkshopPath, ConfigPath

        LocalPath = self.LocalLine.text()
        WorkshopPath = self.WorkshopLine.text()
        ConfigPath = self.CfgLine.text()
        self.close()

class MainWindow(QtGui.QWidget):

    def __init__(self, local, workshop, config):
        super().__init__()
        uic.loadUi('RAMS.ui', self)
        self.localPath = local
        self.workshopPath = workshop
        self.configPath = config
        self.ModList = ModManager.LoadMod(self.localPath) + ModManager.LoadMod(self.workshopPath) #get mod list
        self.setinit()

    def setinit(self):
        self.ActiveKeyList = ModManager.LoadActMod("\\".join([self.configPath, 'Config', 'ModsConfig.xml']))
        CustomItem.LoadItemToList(self.ModList, self.AvailableList, self.A, self.ActiveKeyList) #왜 ActiveList가 작동 안하지?

        self.AvailableList.setAcceptDrops(True)

    def setConnection(self):
        self.OrderSaveBtn.clicked.connect(self.UpdateConfig)

    def UpdateConfig(self):
        length = self.A.count()
        keyList = list()
        for count in range(0, length):
            item = self.A.item(count)
            key = item.data(QtCore.Qt.UserRole)[1] # this have mod key
            keyList.append(key)
        
        ModManager.SaveXML(keyList, self.configPath)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    askscreen = AskWindow()
    askscreen.show()
    app.exec_()

    MainApp = QApplication(sys.argv)
    mainscreen = MainWindow(LocalPath, WorkshopPath, ConfigPath)
    mainscreen.show()

    exit(MainApp.exec_())