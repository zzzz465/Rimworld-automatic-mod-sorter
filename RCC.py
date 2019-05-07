import subprocess, os, sys
from time import sleep
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import CustomItemList, CustomItem
Path = os.path.dirname(__file__)
RCCPath = '\\'.join([Path, 'RCC', 'RCC.exe'])
RCCTextPath = '\\'.join([Path, 'RCC', 'RCC.txt'])
testPath = ('C:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld\\RimWorldWin64.exe', 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld\\Mods', 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\294100')

ModDict = dict()

class Mod:
    def __init__(self, name):
        self.MODname = name
        self.Conflict = dict()

    def addConflictData(self, name, ConflictData):
        try:
            ModCon = self.Conflict[name]
        
        except:
            ModCon = ModConflict(name, self.MODname)
            self.ConflictTo[name] = ModCon
        
        ModCon.addConflict(ConflictData)
    
    def getConflict(self, name):
        try:
            _modconflict = self.Conflict[name]
        
        except:
            _modconflict = ModConflict(name)
            self.Conflict[name] = _modconflict

        return _modconflict

class ModConflict:
    def __init__(self, modname): 
        self.ModName = modname
        self.ConflictTo = list()
        self.ConflictBy = list()

    def addConflictTo(self, data):
        self.ConflictTo.append(data)
    
    def addConflictBy(self, data):
        self.ConflictBy.append(data)

    def ConflictLen(self):
        return len(self.ConflictList)

class ConflictData:
    def __init__(self, Element, DefName):
        self.Element = Element
        self.defName = DefName

def runRCC():
    RCC = subprocess.Popen([], executable=RCCPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    print('success')
    while RCC.poll() is None:
        line = RCC.stdout.readline()
        print(line)
        if 'Complete' in line:
            RCC.kill()
            print('Successfully end program.')
            break

        else:
            pass

#로컬이랑 워크샵이랑 같은 모드가 있으면 충돌로 인식, 제외해야함

def CoreConflictCheck(f): #FIXME
    while True:
        line = f.readline()
        if line == None or '======' in line:
            break
        
        else:
            if 'Conflicting' in line:
                f.readline()
                f.readline() #erase two path line.
                targetLine = f.readline().split() #0번쨰 : 이름, 2번째 배열 위치, 7번쨰 : Line, 9번째 Def, 11번째 Def 엘리먼트, 13번째 DefName
                originLine = f.readline().split()

def LoadActMod(f):
    global ModDict

    line = f.readline() #remove blank line
    while True:
        line = f.readline()
        
        if line == None or '========' in line:
            break
        
        else:
            line = line.split()
            if line[0] == 'Enabled':
                modname = ' '.join(line[9:])
                _mod = Mod(' '.join(line[9:]))
                ModDict[modname] = _mod

            else:
                continue

def XMLConflictHandle(f):
    global ModDict
    while True:
        line = f.readline()
        if line == None or '=======' in line:
            break
        
        elif 'Conflicting' in line:
            f.readline()
            f.readline()
            Upper = f.readline().split()
            Lower = f.readline().split()
            targetName = ' '.join(Upper[:Upper.index('Load')])
            OriginName = ' '.join(Lower[:Lower.index('Load')])
            x, Element, y, defName = Upper[Upper.index('Element:'): Upper.index('Element:') + 4]
            
            try:
                mod1 = ModDict[targetName].getConflict(OriginName) #윗쪽
                mod2 = ModDict[OriginName].getConflict(targetName) #아랫쪽
            
            except:
                print('error')

            ConfData = ConflictData(Element, defName) #to에게 들어갈 것
            mod1.addConflictBy(ConfData)
            mod2.addConflictTo(ConfData)

    return ModDict

def readRCC(filepath=RCCTextPath):
    with open(filepath, mode='r', encoding='UTF-8') as f:
        ModDict = {}
        while True:
            line = f.readline()
            if line == None or line == '':
                break
            
            elif "XML that overwrites 'Core'" in line:
                pass

            elif 'Mods Found' in line:
                LoadActMod(f)
            
            elif 'Checking for XML' in line:
                ModDict = XMLConflictHandle(f)
            
            else:
                pass

    return ModDict

def setConflictChecker(self):
    try:
        CCModList = self.CCModList
    except:
        InfoData = {
            'CCTextBrowser' :self.CCInfo
        }
        self.CCModList = CustomItemList.CCModListWidget(InfoData)
        CCModList = self.CCModList

    layout = self.CCListFrame.layout()
    if layout == None:
        layout = QtWidgets.QGridLayout()

    layout.addWidget(CCModList)
    self.CCListFrame.setLayout(layout)
    for mod in self.ModList:
        if mod.key in self.ActiveKeyList:
            message = func1(self, mod.name)
            CustomItem.CCLoadItemToList(mod, CCModList, message)

    self.CCRefresh.clicked.connect(lambda x : setConflictChecker(self))

def func1(self, modname):
    try:
        ModConflicts = self.ModDict[modname].Conflict
        messages = []
        for conflictData in ModConflict:
            targetAmount = len(conflictData.ConflictTo) #덮어씌우는것
            originAmount = len(conflictData.ConflictBy)
            
            message = """
            {0} mod override {1} mod's data {2}
            {1} mod override {0} mod's data {3}
            """.format(modname, conflictData.ConflictTo.ModName, targetAmount, originAmount)
            messages.append(message)
        
        return messages
    except:
        pass

def main(mainwidget):
    global ModDict
    runRCC()
    readRCC()
    mainwidget.ConflictDict = ModDict

if __name__ == '__main__':
    #runRCC()
    readRCC('C:\\Users\\stopc\\Documents\\Git\\Python\\RAMS\\RCC\\RCC.txt')    
    print(ModDict)