import os
import tkinter as tk
from time import sleep
from tkinter import filedialog

def finder(): # exe 파일, 폴더 찾아서 넘김
    print('please select your rimworld .exe file.')
    print('pop up will open in 2 seconds...')
    cdir = os.path.dirname(os.path.realpath(__file__))
    sleep(2)
    root = tk.Tk()
    rimdir = filedialog.askopenfilename(initialdir = cdir, title = 'Select rimworldwin64.exe', filetype = [('Rimworld.exe file', '*.exe')])
    root.destroy()

    local_mod_folder = '{}/Mods'.format(os.path.dirname(rimdir))

    if os.path.isdir(local_mod_folder) == False:
        print("can't find rimworld mod folder.")
        print('please select local Mod folder.')
        local_mod_folder = finder_folder()
    
    return rimdir, local_mod_folder

def finder_folder(): # 폴더 디렉토리 반환
    print('pop up will open in 2 seconds...')
    sleep(1.5)
    root = tk.Tk()
    dir = filedialog.askdirectory(initialdir = 'C:/', title = 'select folder')
    root.destroy()

    return dir


if __name__ == '__main__':
    dir = finder_folder()
    print(dir)