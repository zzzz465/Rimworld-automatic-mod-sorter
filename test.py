"""
import pickle
import Parse
import mod_sorter
import os
#import mod_parser as mp
os.chdir('C:/Users/Admin/Documents/Python/mod_sorter')
with open('template.bin', 'rb') as f:
    data = pickle.load(f)
mod_dic = {} # 모드와 번호 연결, 번호 : 이름
mod_list_workshop = [] # 모드 리스트(이름만)
config = []
mod_list_sorted = []
mod_dic_num = {} #이름 : 번호
Parse.Parser(mod_dic,mod_dic_num, mod_list_workshop)
config = Parse.mod_sort() # config 리스트에 현재 로딩중인 모드를 리스트로 저장

Parse.Parser(mod_dic, mod_dic_num, mod_list_workshop)

'''
print(mod_dic)
print('\n')
print(mod_list_workshop)
print('\n')
print(config)
print('\n')
print(mod_list_sorted)
print('\n')
print(mod_dic_num)
'''
print(config)

"""
'''
import os
temp = os.path.dirname(os.path.realpath(__file__))
import pickle


dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)
with open('template.bin', 'rb') as f:
    try:
        data = pickle.load(f)
    except EOFError:
        data = dict()

    
data.update(None)
    
with open('template.bin', 'wb') as f:
    pickle.dump(None, f)
'''

import os
a = os.environ['homepath']
os.chdir(a)
os.chdir('./desktop')
import pickle

with open('template.bin', 'rb') as f:
    data = pickle.load(f)

    for i in data:
        print(i, data[i])