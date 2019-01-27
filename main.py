
import os
import shutil
import Parse
from time import sleep
import downloader
import time
import sys
import re
from colorama import init
from colorama import Fore as Color
init(autoreset=True) # colroama 초기화

Version = 0.3
print('현재 버전은 v.' + str(Version) + '입니다.')
print('current program version is v.' + str(Version))
print('\n')
time.sleep(1)

#백업라인
#------------------------------------------------
#VM 머신에선 여기가 없어서 오류가 남...
try:
    temp = os.environ['userprofile']
    rimsavedir = '{}/appdata/locallow/Ludeon Studios\RimWorld by Ludeon Studios\Config'.format(temp)
    os.chdir(rimsavedir)
except:
    print('림월드 SAVE 폴더를 찾을 수 없습니다. 림월드를 설치하신 게 맞나요?')
    print('프로그램을 종료합니다.')

print('기존 컨픽 파일을 백업하는 중...')
print('saving old config files...')
now_time = time.strftime('%d_%H_%M', time.localtime(time.time()))
shutil.copy('ModsConfig.xml', 'ModsConfig.xml.backup{}'.format(now_time))
#------------------------------------------------

print('template를 받아오는 중입니다...')
print('downloading mod DB from github... \n')
data = downloader.update()
data_len = len(data)
print('현재 DB에 등록된 모드의 개수는 ' + Color.GREEN + '{}'.format(data_len) + Color.WHITE + '개 입니다.')
print('DB mod count : ' + Color.GREEN + '{}'.format(data_len))
print('현재 다운받은 파일은 마지막으로 {} 시각에 업데이트 된 파일입니다. 잠시만 기다려 주세요... \n'.format(data['time']))
print('DB last updated time : {} \n'.format(data['time']))
lastest_Version = data['Version']
if Version < lastest_Version:
    print('업데이트 버전이 발견되었습니다. Discord에서 업데이트를 확인해주세요.')
    print('newer version available!, please upgrade.')
    sys.exit(0)

sleep(3)

mod_dic = dict() # 모드와 번호 연결, 번호 : 이름
mod_list_workshop = list() # 모드 리스트(이름만)
mod_dic_num = dict() #이름 : 번호
mod_nlist = list()
mod_list_local = list()

rim64win_path = Parse.Parser(mod_dic,mod_dic_num, mod_list_workshop, mod_list_local, data) # 파싱 작업을 수행 후, 림월드 실행을 위한 파일 경로를 return
print('현재 구독중인 모드 리스트를 불러옵니다...')
print('Loading workshop mods...')

for x in mod_list_workshop:
    sleep(0.05)
    print(Color.LIGHTGREEN_EX + x)
    print('\n')

print('Local 모드 리스트를 불러옵니다...')

for x in mod_list_local:
    sleep(0.05)
    print(Color.LIGHTYELLOW_EX + x)
    print('\n')

config_num = Parse.find_activate_mod() # config 리스트에 현재 로딩중인 모드를 리스트로 저장
print('모드 세팅에서 로딩한 모드를 재배열 합니다...')
print('sorting activated mods....')
sleep(1)

mod_list_sorted = list()
for mod in config_num: #mod는 숫자, 영문이름, 또는 __Localcopy
    m = re.match('__LocalCopy', mod)
    if mod == 'Core':
        continue

    try:
        if m: #만약 config파일에서 불러온 모드의 이름이 __LocalCopy로 시작하면
            modname = mod.split('_')[3]
            mod_list_sorted = mod_list_sorted + [[data[modname], mod, True]]
            print(Color.LIGHTBLUE_EX + 'Localcopy {} 모드를 리스트에 추가'.format(modname))
            print(Color.LIGHTBLUE_EX + 'Add Localcopy {} Mod to list'.format(modname))
            continue


        elif mod.isdigit() == False: #Local인데 __Localcopy가 아니라면
            modname = mod
            mod_list_sorted = mod_list_sorted + [[data[modname], mod, True]]
            print(Color.LIGHTYELLOW_EX + 'local {} 모드를 리스트에 추가'.format(modname))
            print(Color.LIGHTYELLOW_EX + 'Add local {} Mod to list'.format(modname))
            continue

        elif mod.isdigit():
            modname = mod_dic[mod] #mod는 숫자
            mod_list_sorted = mod_list_sorted + [[data[modname], mod, False]]
            print(Color.LIGHTGREEN_EX + 'workshop {} 모드를 리스트에 추가'.format(modname))
            print(Color.LIGHTGREEN_EX + 'add workshop {} mod to list'.format(modname))
            continue


    except:
        print(Color.LIGHTRED_EX + modname + ' 은 template에 없어 제외되었습니다.')
        print(Color.LIGHTRED_EX + modname + "is not supported yet")
        mod_nlist.append(modname)


    finally:
        print('\n')
        sleep(0.2)    

mod_list_sorted.sort()

Parse.setconfig(mod_list_sorted)
print('배열한 모드 순서는 다음과 같습니다.')
print('mods will be loaded in the following order')
print('\n')
for i in mod_list_sorted:
    sleep(0.05)
    if i[2] == False:
        print(Color.LIGHTGREEN_EX + mod_dic[i[1]]) #

    else:
        x = re.match('__Local', i[1])
        if x:
            x = i[1].split('_')
            print(Color.LIGHTBLUE_EX + 'Localcopy {}'.format(x[3]))
        
        else:
            print(Color.LIGHTGREEN_EX + x)

    
        

if len(mod_nlist) != 0:
    print('\n')
    print('\n')
    print('다음 모드는 로드 목록에 있었으나, template에 없어서 로드가 해제된 모드입니다. 인-게임에서 수동으로 모드를 배열해주세요.')
    print('These Mods were in load_list, but not in template. please sort mod manually in game')
    print('\n')
    for x in mod_nlist:
        sleep(0.05)
        print(x)

print('\n')
print('배열이 끝났습니다.')
print('sort complete.')
print('\n')
print('림월드를 실행합니다.')
print('launching Rimworld...')
os.startfile(rim64win_path)

print('로그를 확인해주세요.')
print('please check full log')
exit = False
while exit == False:
    x = input('type "exit" to exit program : ')
    x.lower()
    if x == 'exit':
        exit = True
    else:
        pass





