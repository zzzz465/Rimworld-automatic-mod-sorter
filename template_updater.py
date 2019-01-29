import pickle
import os
import xml.etree.ElementTree as ET
import json
import sys
from time import sleep
import downloader
import time
import tkinter as tk
from tkinter import filedialog
import logging
from colorama import init
from colorama import Fore as Color
import pickle
init(autoreset=True)

def add_dic(template_list, template_dic, template_):
    for temp in template_list: # 모드 리스트를 불러줌
        print('Mod name : {}'.format(temp))

        test = False
        while test == False:
            i = (input('번호는 1~20번입니다. input number 1 to 20 : '))
            if i == 'X' or i == 'x':
                print('작업이 중단되었습니다.')
                print('updating DB inturrpted.')
                breakloop = True
                test = True

            elif i.lower() == 'p':
                print(temp, ' 모드는 보류합니다.')
                print('pass this mod :', temp)
                continue

            try:
                template_dic[temp] = float(i)
                if float(i) > 20 or float(i) < 0:
                    raise ValueError
                print('\n\n')
                test = True
            
            except:
                print('올바르지 않는 입력입니다... 1~20에 해당하는 숫자를 입력해주세요. P or p를 입력하면 패스합니다.')
                print('wrong input... please type 1~20 or X or P')
        
        if breakloop == True:
            break

def Listhandler(template_list): #구독한 모드 리스트 불러오기, template_list에 모드 이름 저장
    root = tk.Tk()
    rim64win_path = filedialog.askopenfilename(initialdir = 'C:/', title = 'Select rimworldwin64.exe', filetype = [('RimworldWin64.exe', 'RimWorldWin64.exe')])
    rim64win_folder = os.path.dirname(rim64win_path)
    root.destroy()

    localmod_path = '{}/Mods'.format(rim64win_folder) #림월드 내 Mods 폴더 경로
    localmod_moddir = os.listdir(localmod_path)


    os.chdir(rim64win_folder)
    os.chdir('../')
    os.chdir('../')
    if os.path.isdir('./workshop/content/294100'):
        os.chdir('./workshop/content/294100')
        moddir = os.listdir('./')
        rimmoddir = os.getcwd() 

        for num in moddir: # num은 모드 번호
            try:
                temp = '{}/{}/About'.format(rimmoddir,num)
                os.chdir(temp) #각 모드의 About 폴더로 이동
                doc = ET.parse('About.Xml') #About.Xml 파싱
                root = doc.getroot()
                name = root.find('name').text # 이름을 저장
                template_list.append(name)
            
            except:
                pass

    for num in localmod_moddir: #num은 모드 번호, local 모드
        try:
            temp = '{}/Mods/{}/About'.format(rim64win_folder,num)
            os.chdir(temp)
            doc = ET.parse('About.xml')
            root = doc.getroot()
            name = root.find('name').text
            template_list.append(name)
        except:
            pass

def sort_num_update(template_dic, overlap_list, nlist): #template_dic는 template에 모드이름 : 번호로 추가, overlap_list는 기존의 template 받아오기
    template_list = []
    Listhandler(template_list)
    len_list = len(template_list)
    len_list = str(len_list)

    print('현재 확인된 모드의 개수는 ' + Color.LIGHTGREEN_EX + '{}'.format(str(len(template_list))) + Color.WHITE + '개 입니다.')
    print('The number of currently identified Mod : ' + Color.LIGHTGREEN_EX + '{}'.format(str(len(template_list))) + Color.WHITE + ' .')
    sleep(0.2)
    
    #중복되는 모드를 제거하는 라인
    print('중복되는 모드를 리스트에서 제거하는 중...')
    print('removing overlap mods...')
    sleep(0.4)
    for val in overlap_list:
        try:
            indexnum = template_list.index(val)
            del template_list[indexnum]
        except:
            pass

    a = os.environ['HOMEPATH']

#보류한 모드 리스트 불러오는 중...  
    os.chdir('C:/')
    os.chdir(a)

    if os.path.isfile('test.db'):
        with open('test.db', 'r') as f:
            overlap_list2 = pickle.load(f)
        

        
        for val in overlap_list2:
                try:
                    indexnum = template_list.index(val)
                    del template_list[indexnum]
                except:
                    pass
    

        
    


        
    len_list = len(template_list)
    len_list = str(len_list)

    
    print(Color.LIGHTGREEN_EX + len_list + Color.WHITE + ' 개의 모드가 확인되었습니다...')
    print(Color.LIGHTGREEN_EX + len_list + Color.WHITE + ' mod need DB update...')
    sleep(0.2)
    print('중단하려면 숫자 대신 X 키를 입력해주세요. P를 입력하면 패스합니다.')
    print('type X to stop updating DB, type P to skip mod. \n')
    print('모드 배열의 순서는 Dcinside Rimworld 갤러리의 닉네임 개념글에서 닉네임 "forge"를 찾아주세요.')
    sleep(0.2)
    breakloop = False
    
    for temp in template_list: # 모드 리스트를 불러줌
        print('Mod name : {}'.format(temp))

        test = False
        while test == False:
            i = (input('번호는 1~20번입니다. input number 1 to 20. : '))
            if i == 'X' or i == 'x':
                print('작업이 중단되었습니다.')
                print('Operation aborted.')
                print('\n\n')
                breakloop = True
                test = True

            elif i.lower() == 'p':
                print(temp, ' 모드는 보류합니다.')
                print('pass this mod : ', temp)
                print('\n\n')
                nlist.append(temp)
                test = True
                continue

            try:
                template_dic[temp] = float(i)
                if float(i) > 20 or float(i) < 0:
                    raise ValueError
                test = True
            
            except:
                print('올바르지 않는 입력입니다... 1~20에 해당하는 숫자를 입력해주세요. P or p를 입력하면 패스합니다.')
                print('wrong input... please type 1~20 or X or P')
            
            finally:
                print('\n')
        
        if breakloop == True:
            break
             

    print('다음과 같은 template를 입력하였습니다.')
    print('you have entered the following template. \n')
    if len(template_dic) != 0:
        for temp in template_dic:
            print(temp,' : ', template_dic[temp]) 

    else:
        if breakloop == False:
            print('이미 Load한 모든 모드가 template에 저장되어있습니다. 프로그램을 종료합니다...')
            print('All the mods you have already loaded are stored in the DB. Quit the program ...')
            sys.exit(0)
        if breakloop == True:
            print('작업을 중단하였습니다. 지금까지 한 작업물을 저장합니다...')
            print('You have stopped working. save db...')

        
#print (os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
        nlist = list()
        downloaded_dic = downloader.update() # 
        template_dic = {}
        temp = False
        while temp == False:
            a = input('Y를 입력하면 모드 번호를 설정하고, N을 입력하면 프로그램을 종료합니다.\n type Y to update DB, N to close the program. Y/N : ')
            if a == 'Y' or a == 'y' :   
                sort_num_update(template_dic, downloaded_dic, nlist)
                temp = True

            elif a == 'N' or a == 'n':
                temp = True

            else:
                print('잘못 입력하였습니다. Y 또는 N만 입력해주세요.\n wrong input. please type Y or N')

        downloaded_dic.update(template_dic)
        #downloaded_dic.update({'time' : '{}'.format(time.ctime())})
        json_val = json.dumps(downloaded_dic) #string 형식

        #테스트 중
        string = str()
        test = json_val.split(',')

        for x in downloaded_dic:
            if x == 'time':
                ctime = time.ctime()
                line =  '\n"{}" : "{}",'.format(x, ctime)
            
            else:
                line = '\n"{}" : {},'.format(x,downloaded_dic[x])

            string = string + line
        
        string = string[:len(string) - 1]

        string = '{' + string + '\n}'

        #테스트 중
        homedir = os.environ['HOMEPATH']
        os.chdir('C:/')
        os.chdir(homedir)
        os.chdir('./desktop')
        if os.path.isfile('db_template.json'):
            os.remove('db_template.json')
            
        with open('db_template.json', 'w', encoding='UTF-8') as f:
            f.write(string)
            f.close()

        with open('nlist.json', 'w', encoding='UTF-8') as f:
            for x in nlist:
                f.write(x)
                f.write('\n')

        print('업데이트된 DB는 바탕화면에 db_template.json 파일로 저장되어있습니다. 개발자에게 전달해주세요')
        print('스킵한 모드 리스트는 바탕화면에 nlist.json 파일로 저장되어있습니다.')
        print('\n The updated DB is saved as db_template.json file on the desktop. Please send it to developer.')
        print('A list of skipped modes can be found in the nlist.json file.(in desktop)')
            

        