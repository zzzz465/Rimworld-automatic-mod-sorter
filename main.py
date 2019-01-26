
import os
import shutil
import Parse
from time import sleep
import downloader
import time
import sys

Version = 0.1

#백업라인
#------------------------------------------------
temp = os.environ['userprofile']
rimsavedir = '{}/appdata/locallow/Ludeon Studios\RimWorld by Ludeon Studios\Config'.format(temp)
os.chdir(rimsavedir)
print('기존 컨픽 파일을 백업하는 중...')
now_time = time.strftime('%d_%H_%M', time.localtime(time.time()))
shutil.copy('ModsConfig.xml', 'ModsConfig.xml.backup{}'.format(now_time))
#------------------------------------------------

print('template를 받아오는 중입니다...')
data = downloader.update()
print('현재 다운받은 파일은 마지막으로 {} 시각에 업데이트 된 파일입니다. 잠시만 기다려 주세요...'.format(data['time']))
lastest_Version = data['Version']
if Version < lastest_Version:
    print('업데이트 버전이 발견되었습니다. Discord에서 업데이트를 확인해주세요.')
    sys.exit(0)

sleep(2)

mod_dic = {} # 모드와 번호 연결, 번호 : 이름
mod_list_workshop = [] # 모드 리스트(이름만)
mod_dic_num = {} #이름 : 번호
mod_nlist = []

rim64win_path = Parse.Parser(mod_dic,mod_dic_num, mod_list_workshop) # 파싱 작업을 수행 후, 림월드 실행을 위한 파일 경로를 return
print('현재 구독중인 모드 리스트를 불러옵니다...')

for x in mod_list_workshop:
    sleep(0.1)
    print(x)

config_num = Parse.mod_sort() # config 리스트에 현재 로딩중인 모드를 리스트로 저장
print('모드 세팅에서 로딩한 모드를 재배열 합니다...')
sleep(1)

mod_list_sorted = list()
for mod in config_num: #mod는 숫자
    if mod == 'Core':
        continue
    try:
        modname = mod_dic[mod] #mod는 숫자
        mod_list_sorted = mod_list_sorted + [[data[modname], mod]]
    except:
        mod_nlist.append(mod)
        print(mod_dic[mod],' 모드는 template에 없어 제외되었습니다.')
        sleep(0.2)
    print('\n')    

mod_list_sorted.sort()

Parse.setconfig(mod_list_sorted)
print('배열한 모드 순서는 다음과 같습니다. \n')
for i in mod_list_sorted:
    sleep(0.1)
    if i[1].isdigit():
        print(mod_dic[i[1]])
    else:
        print(i)

if len(mod_nlist) != 0:
    print('\n')
    print('\n')
    print('다음 모드는 로드 목록에 있었으나, template에 없어서 로드가 해제된 모드입니다. 인-게임에서 수동으로 모드를 배열해주세요.')
    print('\n')
    for x in mod_nlist:
        sleep(0.05)
        print(mod_dic[x])

print('\n')
print('배열이 끝났습니다.')
print('\n')
print('림월드를 실행합니다.')
os.startfile(rim64win_path)




