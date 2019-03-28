import requests
from selenium import webdriver
import os

import fnmatch # for parsing driver's return and get API code. read https://stackoverflow.com/questions/34660530/find-strings-in-list-using-wildcard

webdriver_path = os.path.dirname(os.path.abspath(__file__)) + '\\chromedriver73.exe' # 74, 73, 72로 해서 try ~ except 문을 통한 에러 체크가 필요함.

def main():
    driver = webdriver.Chrome(webdriver_path)
    driver.set_window_size(465, 780) #width 465, height 780 for ideal login size.
    driver.implicitly_wait(3)

    driver.get('https://github.com/login/oauth/authorize?client_id=0bbf2a4e5991a53dfec8')
    
    pattern = "code=*"
    while True:
        list1 = driver.current_url.split('?')
        matching = fnmatch.filter(list1, pattern)

        if matching:
            code = matching[0].split('=')[1]
            driver.quit()
            break

    print(code)

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)) + '\\webdriver73.exe')
    main()