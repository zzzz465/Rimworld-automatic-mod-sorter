from . import ModManager, ItemManager, RWmanager
from PyQt4 import QtGui
import logging
import json

LocalPath = str()
WorkshopPath = str()

log = logging.getLogger('RAMS.mainTool')

def setModPath(RootClass, Qline):
    path = RWmanager.askfolderdir(titlename='choose your mod folder.')
    Qline.setText(path)

    Load_Mod_to_List(path, RootClass.List)

def List_clear(listwidget, local, Workshop):
    listwidget.clear()
    Load_Mod_to_List(local.text(), listwidget)
    Load_Mod_to_List(Workshop.text(), listwidget)

def Load_Mod_to_List(path, listwidget):
    MODlist = ItemManager.Load_Mod(path)
    ItemManager.Add_Mod(MODlist, listwidget)

def changeInfo(Qlistwidget, MyWindow):
    Preview = MyWindow.Preview
    Description = MyWindow.Description
    OrderNumLine = MyWindow.OrderNum

    Item = Qlistwidget.currentItem()
    PreviewPath = Item.data(20)
    Preview.setPixmap(QtGui.QPixmap(PreviewPath)) #이미지 설정
    Description.setText(Item.data(21))

    OrderNumLine.setText(str(Item.data(22)))
    OrderNumLine.setFocus()

#def search(Qlistwidget, searchBox):
#    for x in Qlistwidget.

def EditMode(MyWindow):
    Item = MyWindow.List.currentItem()
    OrderNumLine = MyWindow.OrderNum
    Item.setData(22, OrderNumLine.text())

def EditFinished(self1, self2):
    #sender().

    try:
        row = List.row()
        Next_Item = List.item(row+1)
        List.setCurrentItem(Next_Item)
    
    except:
        pass

def makeDB(Qlistwidget):
    ItemList = []
    log.debug('makeDB 호출')
    try:
        for x in range(1000):
            ItemList.append(Qlistwidget.item(x+1))

    except:
        pass

    mod_dict = dict()

    for Item in ItemList:
        try:
            name = Item.data(23)
            OrderNum = float(Item.data(22).text())

            if OrderNum >= 0.1 and OrderNum < 21:
                mod_dict[name] = OrderNum
    
        except:
            pass

    raw = json.dumps(mod_dict, indent=4)
    
    path = RWmanager.askfolderdir(title='select folder to save...')
    with open('{}/DB_template.json'.format(path), mode='w') as f:
        f.write(raw)
