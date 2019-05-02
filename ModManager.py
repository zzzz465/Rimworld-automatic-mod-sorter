import CustomItem
import os
import xml.etree.ElementTree as ET

class Mod:
    def __init__(name, author, currentVer, description, path):
        self.name = name
        self.author = author
        self.currentVer = currentVer
        self.description = description

def GetTextInXML(path, attribute):
    doc = ET.parse(path)
    root = doc.getroot()
    name = root.find(attribute).text
    
    return name

def LoadMod(ModPath):
    folderList = os.listdir(ModPath)
    ModList = list()

    for folder in folderList:
        AboutPath = '\\'.join([ModPath, folder, 'About', 'About.xml'])

        try:
            name = GetTextInXML(AboutPath, 'name')
            author = GetTextInXML(AboutPath, 'author')
            currentVer = GetTextInXML(AboutPath, 'targetVersion')
            description = GetTextInXML(AboutPath, 'description')
            
            ModList.append(Mod(name, author, currentVer, description))

        except:
            pass


    return ModList 
