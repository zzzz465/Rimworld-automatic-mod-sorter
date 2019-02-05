from colorama import Fore as Color
from colorama import init
import os
from time import sleep


def give_num(ML_active, MD_num_name, MD_name_num, DB): # 배열된 리스트 만들고, 정렬된거랑 정렬안된 리스트 return
    ML_sorted = list()
    ML_error = list()
    try:
        del ML_active[0]

    except:
        pass

    ML_active.append('Core')

    for x in ML_active:
        try:
            if x.isdigit():
                MOD_name = MD_num_name[x]
                ML_sorted.append([[DB[MOD_name], x]])
                print(Color.LIGHTGREEN_EX + 'Add workshop mod to the list. >> {}'.format(MOD_name))
            
            else:
                MOD_name = MD_num_name[x]
                ML_sorted.append([[DB[MOD_name], x]])
                print(Color.LIGHTYELLOW_EX + 'Add local mod to the list. >> {}'.format(MOD_name))

        except:
            print(Color.LIGHTRED_EX + MD_num_name[x] + ' is not supported yet.')
            ML_error.append(MD_num_name[x])

        finally:
            print('\n')
            sleep(0.05)

    ML_sorted.sort()
    ML_error.sort()

    return ML_sorted, ML_error

    


    
                
            


