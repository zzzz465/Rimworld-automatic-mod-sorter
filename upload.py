#!/usr/bin/python
import os, requests, sys, json, time

def gitupload():
    time.sleep(5)
    print('please wait...')
    username='RAMSlog'
    password='githubgistRAMSlog'
    filename = 'RAMS_Log.txt'

    content=open(filename, 'r').read()
    r = requests.post('https://api.github.com/gists',json.dumps({'files':{filename:{"content":content}}}),auth=requests.auth.HTTPBasicAuth(username, password)) 
    print(r.json()['html_url'])

if __name__ == '__main__':
    gitupload()