from . import WebLogin
from ... import RWmanager
import json
from time import sleep
import logging
import os

client_id = '663a6cf8eeff353b0625'
gitAuthurl = 'https://github.com/login/oauth/authorize?client_id=663a6cf8eeff353b0625'
data_path = os.path.dirname(os.path.abspath(__file__)) + '\\data.json'

log = logging.getLogger('RAMS.core.API.Auth.GitAuth')

def issue_token():
    '''
    make user to login Github, and write token to data.json file
    '''

    driver = WebLogin.get_webdriver()
    log.debug('webdriver loaded.')
    driver.get(gitAuthurl)
    log.debug('connect to {}'.format(gitAuthurl))
    driver.implicitly_wait(3)

    code = get_code(driver)
    log.debug('code : {}'.format(code))

    RWmanager.write_data(data_path, 'token', code)

def get_code(driver):
    '''
    prase driver's url and read code \n
    return code (str type)\n
    raise timeout error after 2 min
    '''
    import fnmatch
    pattern = "code=*"

    log.debug('waiting for token url...')
    while True:
        timer = 0

        url = driver.current_url.split('?')
        matching = fnmatch.filter(url, pattern)

        if matching:
            code = matching[0].split('=')[1]
            log.debug('token : {}'.format(code))
            return code

        else:
            sleep(0.5) #check url in every 0.5 seconds.
        
        timer += 0.5

        if timer > 120:
            log.warning('time out error.')
            raise TimeoutError
            break

def get_token():
    """
    return token in data.
    raise Error if can't load token
    """
    log.debug('load token...')
    with open(data_path, mode='r') as f:
        token = json.loads(f.read())['token'] 
        return token

