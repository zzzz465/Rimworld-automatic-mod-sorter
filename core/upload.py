import urllib.request
import json
import datetime
import time
import logging


def gitupload(str1, token):
    '''
    HTTP Reuests has following parameters: 
    1)Request URL 
    2)Header Fields
    3)Parameter 
    4)Request body
    '''
    #!/usr/bin/env python

    import requests
    #from urllib import request as requests
    import json

    GITHUB_API="https://api.github.com"
    API_TOKEN=str(token)

    #form a request URL
    url=GITHUB_API+"/gists"
    print("Request URL: %s"%url)

    #print headers,parameters,payload
    headers={'Authorization':'token %s'%API_TOKEN}
    params={'scope':'gist'}
    payload={"description":"GIST created by python code","public":True,"files":{"RAMS log file":{"content":"{0}".format(str1)}}}

    #make a requests
    res=requests.post(url,headers=headers,params=params,data=json.dumps(payload))

    #print response --> JSON
    #token = 
    print('status code : {}'.format(res.status_code))
    j=json.loads(res.text)

    # Print created GIST's details


if __name__ == '__main__':
    test_text ="""
    log file text
    asdf
    adsf2a
    sdfsdf
    Modname3
    modmane4
    asdfffdsfsfsfsfd
    """
    print('initializing')
    #gitupload(test_text)