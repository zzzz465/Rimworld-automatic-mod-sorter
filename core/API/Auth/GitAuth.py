import json
from time import sleep
import logging
import os

client_id = '663a6cf8eeff353b0625'
gitAuthurl = 'https://github.com/login/oauth/authorize?client_id=663a6cf8eeff353b0625'
appdata = os.environ['appdata']
data_path = appdata + '\\RAMS\\Auth' + '\\data.json'

log = logging.getLogger('RAMS.core.API.Auth.GitAuth')

def write_data(key, value):
    '''
    write key, value to data.json file in Auth
    '''

    if os.path.isdir(os.path.dirname(data_path)) != True:
        os.mkdir(os.path.dirname(data_path))

    with open(data_path, mode='r') as f:
        data = json.loads(f.read())

    with open(data_path, mode='w') as f:
        data[key] = value
        f.write(json.dumps(data))

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

    write_data(data_path, 'token', code)

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

def load_token():
    """
    return token in data.
    raise Error if can't load token
    """
    log.debug('load token...')
    try:
        with open(data_path, mode='r') as f:
            token = json.loads(f.read())['token'] 
            return token

    except Exception as e:
        log.error('Exception : {}'.format(e))
        raise e

def get_code():
    '''
    return token
    '''

    try: #try to load code from data.json file
        token = load_token()
        return token

    except:
        token = issue_token()
    
    return token