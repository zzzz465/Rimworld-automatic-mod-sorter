import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4 import QtGui
from Core import mainTool as MT
from Core import downloader
import logging

log = logging.getLogger('RAMS')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s',"%H:%M:%S")
log.setLevel(logging.INFO)
log.addHandler(stream_handler)
log.propagate = 0
stream_handler.setFormatter(formatter)

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        DB = downloader.download_DB()
        
        self.setinit()


    def setinit(self):
        self.connection()
        self.OrderNum.setValidator(QtGui.QDoubleValidator())

    def connection(self):
        self.LocalBtn.clicked.connect(lambda x : MT.setModPath(self, self.LocalPath)) #버튼 누르면 경로 저장
        self.WorkshopBtn.clicked.connect(lambda x : MT.setModPath(self, self.WorkshopPath))

        self.Refresh.clicked.connect(lambda x : MT.List_clear(self.List, self.LocalPath, self.WorkshopPath))
        
        self.List.currentItemChanged.connect(lambda x : MT.changeInfo(self.List, self))

        self.OrderNum.textChanged.connect(lambda x : MT.EditMode(self))
        #self.OrderNum.returnPressed.connect(lambda x : MT.EditFinished(self, self))
        #self.SetValue.clicked.connect(lambda x : MT.EditFinished(self, self)) #왜 작동 안하지? FIXME

        self.Save.clicked.connect(lambda x : MT.makeDB(self.List))

def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

if __name__ == '__main__':
    log.info('start program...')
    main()