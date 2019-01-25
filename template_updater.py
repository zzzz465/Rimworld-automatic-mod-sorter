import pickle
import os
import xml.etree.ElementTree as ET
import json
import sys
from time import sleep
import downloader
def file_check(): # 필요가 없어짐
    dir = os.environ['homepath']
    os.chdir(dir)
    os.chdir('./desktop')
    #print(os.getcwd())
    if os.path.isfile('./db_template.json'):
        print('json 파일을 바탕화면에서 발견하였습니다.')

        f = open('db_template.json', 'r')
            
        try:
            template_num = len(json.loads(f.read()))
            
        except:
            f.close()
            f = open('db_template.json', 'w')
            temp_1 = {}
            temp_1 = json.dumps(temp_1)
            f.write(temp_1)
            f.close()
                

        print(template_num,' 개의 모드를 template.json에서 발견하였습니다.')
    
    else:
        with open('db_template.json', 'w') as f:
            f.write('{}')
            f.close() #파일 없으면 만들기
        print('파일을 발견하지 못했습니다. 비어있는 json 파일을 바탕화면에 생성중...')
    return 


def Listhandler(template_list): #구독한 모드 리스트 불러오기, template_list에 모드 이름 저장
    rimmoddir = 'C:/Program Files (x86)\Steam\steamapps/workshop/content/294100'
    moddir = os.listdir('C:\Program Files (x86)\Steam\steamapps/workshop/content/294100')
    for mod in moddir: # mod는 모드 번호
        temp = '{}/{}/About'.format(rimmoddir,mod)
        os.chdir(temp) #각 모드의 About 폴더로 이동
        #print(temp)
        doc = ET.parse('About.Xml') #About.Xml 파싱
        root = doc.getroot()
        name = root.find('name').text # 이름을 저장
        template_list.append(name)

def sort_num_update(template_dic, overlap_list):
    template_list = []
    Listhandler(template_list)

    print('현재 확인된 모드의 개수는 {}개 입니다.'.format(len(template_list)))
    sleep(0.1)
    
    #중복되는 모드를 제거하는 라인
    '''
    dir = os.environ['homepath']
    os.chdir(dir)
    os.chdir('./desktop')
    f = open('db_template.json', 'r')
    try:
        overlap_list = json.loads(f.read())
    except:
        pass
    '''
    
    print('중복되는 모드를 리스트에서 제거하는 중...')
    sleep(0.4)
    for val in overlap_list:
        try:
            indexnum = template_list.index(val)
            del template_list[indexnum]
        except:
            pass

    
    print(len(template_list), ' 개의 모드가 확인되었습니다...')
    sleep(0.2)
    print('중단하려면 숫자 대신 X 키를 입력해주세요')
    sleep(0.2)
    for temp in template_list: # 모드 리스트를 불러줌
        print('Mod name : {}'.format(temp))
        test = False
        while test == False:
            i = (input('번호는 1~16번입니다. : '))
            #import random
            #i = random.randrange(1,16)
            if i == 'X' or i == 'x':
                print('작업이 중단되었습니다.')
                sys.exit(1)
            try:
                template_dic[temp] = int(i)
                test = True
                if int(i) > 20 or int(i) < 0:
                    raise ValueError
                print('\n\n')
            
            except:
                print('올바르지 않는 입력입니다... 1~20에 해당하는 숫자를 입력해주세요.')

    print('다음과 같은 template를 입력하였습니다.\n')
    if len(template_dic) != 0:
        for temp in template_dic:
            print(temp,' : ', template_dic[temp]) 

    else:
        print('이미 로드한 모든 모드가 template에 저장되어있습니다. 프로그램을 종료합니다...')
        sys.exit(0)

        
#print (os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    overlap_list = downloader.update()
    template_dic = {}
    temp = False
    while temp == False:
        a = input('Y를 입력하면 모드 번호를 설정하고, N을 입력하면 모드 template를 업데이트합니다. Y/N : ')
        if a == 'Y' or a == 'y' :   
            sort_num_update(template_dic, overlap_list)
            temp = True

        elif a == 'N' or a == 'n':
            temp = True

        else:
            print('잘못 입력하였습니다. Y 또는 N만 입력해주세요.')

    dic_old = {}
    try:
        f = open('db_template.json', 'r')
        dic_old = json.loads(f.read())
        if dic_old == None:
            dic_old = {}
    
    except:
        with open('db_template.json', 'w') as f:
            f.close() # 이 코드를 지워도 되나?

    dic_old.update(template_dic)
    json_val = json.dumps(dic_old) #string 형식

    with open('db_template.json', 'w') as f:
        f.write(json_val)
        f.close()
    
'''    
    #data.update(template_dic)

    #print(template_dic)
    
    with open('template.bin', 'wb') as f:
        pickle.dump(template_dic, f)
'''

