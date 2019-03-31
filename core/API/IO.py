import requests
import json
import os
from urllib.request import urlopen

DBurl = 'https://github.com/RAMSlog/RAMS_DB/raw/master/working_DB.json'
NModurl= 'https://github.com/RAMSlog/RAMS_DB/raw/master/NMODS.json'

def get_working_DB():
    '''
    get DB from RAMSlog Dev RAMS_DB DB.json
    '''
    with urlopen(DBurl) as DBraw:
        DB = json.loads(DBraw.read())

    return DB

def get_NMODlist():
    '''
    get nMod list from RAMS_DB
    '''

    with urlopen(NModurl) as NMODraw:
        Nmod = json.loads(NMODraw.read())

    return Nmod

def set_working_DB(DB, token):
    pass

    api_url = 'https://api.github.com/repos/RAMSlog/RAMS_DB'
    

def test():
    print(get_working_DB())
    print(get_NMODlist())

if __name__ == '__main__':
    test()

