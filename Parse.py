import xml.etree.ElementTree as ET
import os
from lxml import etree
#파이썬에서 환경변수를 지원 안함? 아니다. os.environ 사용
#mod_dic = {} # 테스트용
#mod_list = [] # 테스트용

rimmoddir = 'C:/Program Files (x86)\Steam\steamapps/workshop/content/294100'
os.chdir(rimmoddir)
moddir = os.listdir('C:\Program Files (x86)\Steam\steamapps/workshop/content/294100')
temp = os.environ['userprofile']
rimsavedir = '{}/appdata/locallow/Ludeon Studios\RimWorld by Ludeon Studios\Config'.format(temp)

def Parser(mod_dic,mod_dic_num, mod_list_workshop): #mod_dic : 모드 이름과 번호를 연결, mod_list는 실제 가지고있는 모드 리스트(이름으로)
        #mod_list_workshop는 창작마당에 있는 모드 리스트 불러오기
    for num in moddir: # mod는 모드 번호
        temp = '{}/{}/About'.format(rimmoddir,num)
        os.chdir(temp) #각 모드의 About 폴더로 이동
        doc = ET.parse('About.Xml') #About.Xml 파싱
        root = doc.getroot()
        name = root.find('name').text # 이름을 저장
        mod_list_workshop.append(name)
        #print(name)
        mod_dic[num] = name #번호 : 이름
        mod_dic_num[name] = num


def setconfig(m_s,): # 소팅된 모드를 받아오기, 세팅 xml을 수정, config은 사용중인 모드 리스트 출력        
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


def mod_sort():
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