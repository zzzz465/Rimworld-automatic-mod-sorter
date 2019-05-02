import CustomItem
import os
import xml.etree.ElementTree as ET

class Mod:
    def __init__(self, name, modkey, author, currentVer, description, path):
        self.name = name
        self.key = modkey
        self.author = author
        self.currentVer = currentVer
        self.description = description

def GetTextInXML(path, attribute):
    try:
        doc = ET.parse(path)
        root = doc.getroot()
        name = root.find(attribute).text
    
    except:
        return 'ValueError'
    
    return name

def LoadMod(ModListPath):
    folderList = os.listdir(ModListPath)
    ModList = list()

    for folder in folderList:
        ModPath = '\\'.join([ModListPath, folder])
        AboutPath = '\\'.join([ModPath, 'About', 'About.xml'])

        try:
            name = GetTextInXML(AboutPath, 'name')
            author = GetTextInXML(AboutPath, 'author')
            currentVer = GetTextInXML(AboutPath, 'targetVersion')
            description = GetTextInXML(AboutPath, 'description')
            modkey = folder
            x = Mod(name, folder, author, currentVer, description, ModPath)
            ModList.append(x)

        except Exception as e:
            print(e)
            pass


    return ModList

def LoadActMod(root):
    """
        accept ET root for argument\n
        return list of mod key
    """
    root = ET.parse(root)
    ActiveMod = root.find("activeMods")
    active_mod = list()

    for li in ActiveMod.findall("li"):
        active_mod.append(str(li.text))

    return active_mod  # Modkey를 반환

def SaveXML(KeyList, configPath):
    ConfigFilePath = '\\'.join([configPath, 'Config', 'ModsConfig.xml'])
    doc = ET.parse(ConfigFilePath)
    root = doc.getroot()

    root.remove(root.find("activeMods")) #remove all mod list
    ActiveMods = ET.SubElement(root, "activeMods")

    for x in KeyList:
        mod = ET.SubElement(ActiveMods, "li")
        mod.text = str(x)

    doc.write("ModsConfig.xml", encoding='UTF-8', xml_declaration='False')

if __name__ == '__main__':
    pass