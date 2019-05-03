import os, json

configPath = '\\'.join([os.environ['APPDATA'], 'RimLOT'])

def FileCheck():
    FolderCheck()
    filepath = '\\'.join([configPath, 'RimLOTConfig.json'])
    if os.path.isfile(filepath):
        pass

    else:
        with open(filepath, mode='w') as f:
            f.write(r'{}')

def FolderCheck():
    try:
        os.makedirs(configPath)

    except:
        pass

def WriteConfig(key, value):
    FolderCheck()
    FileCheck()
    filepath = '\\'.join([configPath, 'RimLOTConfig.json'])
    config = dict()

    with open(filepath, mode='r') as f:
        raw = f.read()
        config = json.loads(raw)

    config[key] = value

    with open(filepath, mode='w') as f:
        f.write(json.dumps(config, indent=4))

def ReadConfig(*Keys):
    filepath = '\\'.join([configPath, 'RimLOTConfig.json'])
    if os.path.isfile(filepath):
        KeyList = list()
        for Key in Keys:
            with open(filepath, mode='r') as f:
                try:
                    raw = f.read()
                    config = json.loads(raw)
                    KeyList.append(config[Key])

                except:
                    KeyList.append(' ')
        
        return tuple(KeyList)

    else:
        return map(lambda x : ' ', [x for x in range(len(Keys))])