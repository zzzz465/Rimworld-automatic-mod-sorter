import finder
from time import sleep
import json
import time
import os

def overlap_remover(DB, M_list):
    returnlist = list()
    for x in M_list:
        if x in DB:
            continue
        else:
            returnlist.append(x)

    return returnlist

def isfloat(num):
    try:
        float(num)
        return True

    except:
        return False

def mod_update(MD_list):
    template = dict()
    for x in MD_list:
        print('Mod name : ' + x)
        breakloop = True
        while breakloop:            
            _input = input('input 1 ~ 20 : ')

            if isfloat(_input):                
                if float(_input) > 20 or float(_input) < 0:
                    print('wrong input. ')
                
                else:
                    template[x] = _input
                    breakloop = False

            elif _input.isalpha():
                if _input == 'S' or _input == 's':
                    breakloop = False
            
            print('\n')
        
    return template

def DB_update(DB_old, DB_new):
    DB_old.update(DB_new)

def DB_save(DB):
    print('please select directory to save DB file.')
    sleep(2)
    savedir = finder.finder_folder()

    DB['time'] = str(time.ctime())
    string = str()
    for x in DB:
        line = '\n"{}" : {},'.format(x,DB[x])
        string = string + line

    string = string[:len(string) - 1]
    string = '{' + string + '\n}'

    os.chdir(savedir)

    with open('db_template.json', 'w', encoding='UTF-8') as f:
        f.write(string)

    print('your file has stored in directory : ' + savedir)
    print('please send file to developer.')
    print('Ludeon forum, steam workshop page or discord')




if __name__ == '__main__':
    pass