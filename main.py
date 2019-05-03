import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog, QApplication

import ModManager, RWManager, CustomItem, CustomItemList
WorkshopPath = str()
LocalPath = str()
ConfigPath = str()

Style = '''
    QWidget {
        
    }'''

class AskWindow(QtGui.QWidget):
    global WorkshopPath, LocalPath, ConfigPath

    def __init__(self):
        super().__init__()
        uic.loadUi("askDialog.ui", self)
        
        self.setInit()
        self.setConnection()

    def setInit(self):
        Local, Workshop, Config = RWManager.ReadConfig('LocalPath', 'WorkshopPath', 'ConfigPath')
        self.LocalLine.setText(Local)
        self.WorkshopLine.setText(Workshop)
        self.CfgLine.setText(Config)

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
        RWManager.WriteConfig('LocalPath', LocalPath)
        RWManager.WriteConfig('WorkshopPath', WorkshopPath)
        RWManager.WriteConfig('ConfigPath', ConfigPath)
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

        self.setStyleSheet(Style)

    def setinit(self):
        self.AvailableList = CustomItemList.ModListWidget()
        self.AvailableListLayout.addWidget(self.AvailableList, 1)
        self.ActiveList = CustomItemList.ModListWidget()
        self.ActiveListLayout.addWidget(self.ActiveList, 1)

        self.ActiveKeyList = ModManager.LoadActMod("\\".join([self.configPath, 'Config', 'ModsConfig.xml']))
        CustomItem.LoadItemToList(self.ModList, self.AvailableList, self.ActiveList, self.ActiveKeyList) #왜 ActiveList가 작동 안하지?

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

def main():
    app = QApplication(sys.argv)
    askscreen = AskWindow()
    askscreen.show()
    app.exec_()

    MainApp = QApplication(sys.argv)
    mainscreen = MainWindow(LocalPath, WorkshopPath, ConfigPath)
    mainscreen.show()

    exit(MainApp.exec_())

def test():
    LocalPath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld\\Mods'
    WorkshopPath = 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\294100'
    ConfigPath = 'C:\\Users\\stopc\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios'
    MainApp = QApplication(sys.argv)
    mainscreen = MainWindow(LocalPath, WorkshopPath, ConfigPath)
    mainscreen.show()

    exit(MainApp.exec_())


if __name__ == '__main__':
    test()