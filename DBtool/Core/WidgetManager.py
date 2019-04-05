from PyQt4 import QtGui

class ModList(QtGui.QWidget): #리스트 프레임을 만든다. 상단에는 검색 창, 하단에는 아이템을 받을 수 있는 리스트를 만듬.
    def __init__(self):
        super().__init__()

        self.RootLayout = QtGui.QVBoxLayout()
        
        self.searchbox = QtGui.QTextEdit()
        self.ListWidget = QtGui.QListWidget()

        self.RootLayout.addWidget(self.searchbox)
        self.RootLayout.addWidget(self.ListWidget)

        self.setLayout(self.RootLayout)

def main():
    modlist = ModList()

if __name__ == '__main__':
    main()