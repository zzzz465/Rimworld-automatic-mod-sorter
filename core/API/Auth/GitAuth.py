import WebLogin
import json
import os

data_path = os.path.dirname(__file__) + '\\data.json'

def read_token():
    '''
    read token in data.json file
    return token if available.
    raise ValueError if the value is blank.
    '''
    with open(data_path, mode='r') as f:
        raw = f.read()
        data_dict = json.loads(raw)
        
        if data_dict['token']:
            return data_dict['token']

        else:
            raise ValueError

def write_token(token):
    '''
    write token to data.json file.
    "token" : " ~~token~~ "
    '''
    with open(data_path, mode='r') as f:
        data_dict = json.loads(f.read())
        data_dict['token'] = token
        
    with open(data_path, mode='w') as f:
        f.write(json.dumps(data_dict, indent=4))

def test():
    #with open(data_path, mode='r') as f:
    #    print(f.read())
    #    print(type(f.read()))

    #print(data_path)

    param = "test token"
    write_token(param)


if __name__ == '__main__':
    test()
