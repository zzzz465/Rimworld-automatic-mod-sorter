#-*- coding:utf-8 -*-
import urllib.request
import json
import datetime
import time
import logging


def gitupload(str1):
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

    #form a request URL
    url=GITHUB_API+"/gists"
    print("Request URL: %s"%url)

    #print headers,parameters,payload
    params={'scope':'gist'}
    now_time = time.strftime("%H : %M : %S")
    payload={"description":"RAMSlog upload, time : {}".format(now_time),"public":True,"files":{"RAMS log file":{"content":"{0}".format(str1)}}}

    #make a requests
    res=requests.post(url,auth=requests.auth.HTTPBasicAuth(username='RAMSlog', password='githubgistRAMSlog') ,params=params,data=json.dumps(payload))

    #print response --> JSON
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