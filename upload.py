import urllib.request
import json
import datetime
import time

def gitupload(str1):
    token = "7d89a919a84024682af376874e0535444d72ea8d"
    access_url = "https://api.github.com/gists"

    filename = "RAMS_nMODlist.txt"
    description = "description"
    public = "true"

    information = "information"
    date = datetime.date.today()
    current_time = time.strftime("%H:%M:%S")

    data = """{
    "description": "%s",
    "public": %s,
    "files": {
        "%s": {
        "content": "{}"
            }w
        }
    }""".format(str1)

    json_data = data % (description, public, filename, information, date, current_time)

    req = urllib.request.Request(access_url)
    req.add_header("Authorization", "token {}".format(token))
    req.add_header("Content-Type", "application/json")
    urllib.request.urlopen(req, data=json_data)