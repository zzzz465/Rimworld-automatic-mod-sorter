from PyQt4 import QtGui

class CustomWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        self.QGridLayout = QtGui.QGridLayout()
        self.ModName = QtGui.QLabel()
        self.ModAuthor = QtGui.QLabel()
        self.Icon = QtGui.QLabel()

        self.QGridLayout.addWidget(ModName, 0, 0)
        self.QGridLayout.addWidget(ModAuthor, 0, 1)
        self.QGridLayout.addwidget(Icon, 1, 0)

    def setModName(self, text):
        self.ModName.setText(text)

    def setModAuthor(self, text):
        self.ModAuthor.setText(text)

    def setIcon(self, bool): #TODO 스팀 ->1, 로컬 -> 0
        if bool == True:
            pass
        
        else:
            pass