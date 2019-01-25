import os
import xml.etree.ElementTree as etree
import Parse

def num_grant(mod_list, mod_list_sorted, template, mod_dic):
    mod_list_sorted = [] # 초기화
    for mod in mod_list: #mod에 mod_list에 있는 모드 이름을 대입, mod_list는 모드의 문자열(이름)
        if mod in template: # template에 이름이 있으면
            try:
                mod_list_sorted.append([[template[mod], mod_dic[mod]]]) #리스트에 추가, [번호, 이름]
            except KeyError as e:
                pass




if __name__ == '__main__':
    pass

