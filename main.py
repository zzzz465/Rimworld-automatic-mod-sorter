
import os
import shutil
import pickle
import Parse
from time import sleep
import downloader
#백업라인
#------------------------------------------------
temp = os.environ['userprofile']
rimsavedir = '{}/appdata/locallow/Ludeon Studios\RimWorld by Ludeon Studios\Config'.format(temp)
os.chdir(rimsavedir)
print('기존 컨픽 파일을 백업하는 중...')
for i in range(99):
    if os.path.exists('ModsConfig.xml.backup{}'.format(i)) == True:
        continue

    else:
        shutil.copy('ModsConfig.xml', 'ModsConfig.xml.backup{}'.format(i))
        break
#------------------------------------------------

print('template를 받아오는 중입니다...')
data = downloader.update()
print('현재 다운받은 파일은 마지막으로 {} 시각에 업데이트 된 파일입니다. 잠시만 기다려 주세요...'.format(data['time']))
sleep(2)

mod_dic = {} # 모드와 번호 연결, 번호 : 이름
mod_list_workshop = [] # 모드 리스트(이름만)
mod_dic_num = {} #이름 : 번호
mod_nlist = []

Parse.Parser(mod_dic,mod_dic_num, mod_list_workshop)
print('현재 구독중인 모드 리스트를 불러옵니다...')

for x in mod_list_workshop:
    sleep(0.1)
    print(x)

config_num = []
config_num = Parse.mod_sort() # config 리스트에 현재 로딩중인 모드를 리스트로 저장
print('모드 세팅에서 로딩한 모드를 재배열 합니다...')
sleep(1)
Parse.Parser(mod_dic, mod_dic_num, mod_list_workshop)

mod_list_sorted = []
for mod in config_num:
    if mod in mod_dic:
        modname = mod_dic[mod] #mod는 숫자
        mod_list_sorted = mod_list_sorted + [[data[modname], mod]]

    else:
        if mod == 'Core':
            print('Core')

        else:
            modname = mod_dic[mod]
            mod_nlist.append(modname)

        

mod_list_sorted.sort()

Parse.setconfig(mod_list_sorted)
print('배열한 모드 순서는 다음과 같습니다. \n')
for i in config_num:
    sleep(0.1)
    if i.isdigit():
        print(mod_dic[i])
    else:
        print(i)

if mod_nlist == True:
    print('다음 모드는 로드 목록에 있었으나, template에 없어서 로드가 해제된 모드입니다. 인-게임에서 수동으로 모드를 배열해주세요.')
    for x in mod_nlist:
        print(x)


print('배열이 끝났습니다.')


