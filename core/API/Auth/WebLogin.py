from selenium import webdriver
import os

driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Chromedriver_list = ['chromedriver74.exe', 'chromedriver73.exe', 'chromedriver72.exe']
IEdriver = 'IEDriverServer.exe'

def get_webdriver():
    '''
    return Chrome webdriver (if it isn't available, return Internet explorer webdriver)
    '''
    for name in Chromedriver_list:
        try:
            path = driver_path + '\\' + name
            driver = webdriver.Chrome(path)
            driver.set_window_size()

            return driver
        
        except:
            continue
        
    driver = webdriver.Ie(driver_path + IEdriver)

    return driver

def test():
    driver = get_webdriver()

if __name__ == '__main__':
    test()
    

    