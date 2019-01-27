import xml.etree.ElementTree as ET
import os
from lxml import etree
import tkinter as tk
from tkinter import filedialog
import re
#파이썬에서 환경변수를 지원 안함? 아니다. os.environ 사용
#mod_dic = {} # 테스트용
#mod_list = [] # 테스트용

temp = os.environ['userprofile']
rimsavedir = '{}/appdata/locallow/Ludeon Studios\RimWorld by Ludeon Studios\Config'.format(temp)


def Parser(mod_dic,mod_dic_num, mod_list_workshop, mod_list_local, data): #mod_dic : 모드 이름과 번호를 연결, mod_list는 실제 가지고있는 모드 리스트(이름으로)
        #mod_list_workshop는 창작마당에 있는 모드 리스트 불러오기
        #data로 현재 template을 받아옴
        print('please select your rimworld exe file.')
        root = tk.Tk()
        rim64win_path = filedialog.askopenfilename(initialdir = 'C:/', title = 'Select rimworldwin64.exe', filetype = [('RimworldWin64.exe', 'RimWorldWin64.exe')])
        rim64win_folder = os.path.dirname(rim64win_path)
        root.destroy()
        
        localmod_path = '{}/Mods'.format(rim64win_folder) #림월드 내 Mods 폴더 경로
        local_moddir = os.listdir(localmod_path)

        os.chdir(rim64win_folder)
        os.chdir('../')
        os.chdir('../')
        os.chdir('./workshop/content/294100')
        rimmoddir = os.getcwd()
        moddir = os.listdir('./')  # 모드 번호 (폴더로)  
        mod_dic_num['Core'] = 'Core'    
        for num in moddir: # mod는 모드 번호, workshop 파일 불러오기
                try:
                        temp = '{}/{}/About'.format(rimmoddir,num)
                        os.chdir(temp) #각 모드의 About 폴더로 이동
                        doc = ET.parse('About.Xml') #About.Xml 파싱
                        root = doc.getroot()
                        name = root.find('name').text # 이름을 저장
                        mod_list_workshop.append(name)
                        #print(name)
                        mod_dic[num] = name #번호(config 파일용) : 이름
                        mod_dic_num[name] = num # 이름 : 번호(config 파일용)
                except Exception as e:
                        print('Error appear! ', e)

        for num in local_moddir:
                m = re.match('__LocalCopy', num)
                try:
                        if m:
                                folder_name = num.split('_')[3] 
                        else:
                                folder_name = num                       
                        temp = '{}/{}/About'.format(localmod_path,num)
                        os.chdir(temp)
                        doc = ET.parse('About.xml')
                        root = doc.getroot()
                        name = root.find('name').text
                        mod_list_local.append(name)
                        mod_dic[num] = name

                except Exception as e:
                        print('Error occur! ', e)

                 
        
        
        mod_dic['Core'] = 'Core'
        return rim64win_path # 림월드 실행을 위해 파일 경로를 반환
        



def setconfig(m_s): # 소팅된 모드를 받아오기, 세팅 xml을 수정        
        os.chdir(rimsavedir)
        doc = ET.parse('ModsConfig.xml')
        root = doc.getroot()

        activeMod = root.find('activeMods')

        for li in activeMod.findall('li'):
                activeMod.remove(li) #모드배열 초기화
       
        #print(ET.dump(root)) 
        sorted_mod = ET.SubElement(activeMod, 'li')
        sorted_mod.text = str('Core')
        for value in m_s: #m_s는 소팅된 모드 리스트를 받아옴, [순서(숫자), 모드 번호] 형식이어야함
                sorted_mod = ET.SubElement(activeMod, 'li')
                sorted_mod.text = str(value[1])
        # 모드 입력은 잘 되는데, 깔끔하지가 않음 개선해야함

        doc.write('ModsConfig.xml', encoding='UTF-8', xml_declaration='false')


def find_activate_mod(): #config 파일에서 active된 모드 리스트 가져오는 함수
        '''template는 이름 : 번호
           config는 컨픽파일에 있는 모드 리스트 불러오기
        '''
        config = []
        os.chdir(rimsavedir)
        doc = ET.parse('ModsConfig.xml')
        root = doc.getroot()
        activeMod = root.find('activeMods')

        for li in activeMod.findall('li'): 
                config.append(str(li.text)) # 현재 config 파일에 있는 모드 리스트를 가져옴
        
        return config


        


if __name__ == '__main__':
        pass