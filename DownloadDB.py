# -*- coding:utf-8 -*-
import json
import os
import sys
from time import sleep
from urllib.request import urlopen
import logging

DB_url = "https://raw.githubusercontent.com/zzzz465/Rimworld-automatic-mod-sorter/master/db_template.json"

#log = logging.getLogger("RAMS.downloader")


def download_DB():  # shakeyourbunny's code. thank you!
    try:
        """Return latest DB file type <dict>
        """
        #log.info("fetching latest DB file from server...")
        #log.info("please allow firewall internet connection.")
        sleep(1)
        with urlopen(DB_url) as jsonurl:
            dbrawdata = jsonurl.read()

        #log.info("DB download complete!")

        return json.loads(dbrawdata)

    except Exception:
        pass
        #try:
        #    #log.warning(
        #    #    "cannot download DB from server. loading local DB files..."
        #    #)
        #    #currentpath = os.getcwd()  # 설마..

        #    with open("DB_template.json", mode="r") as jsonlocal:
        #        dbrawdata = jsonlocal.read()

        #    return json.loads(dbrawdata)

        #except Exception:
        #    pass


if __name__ == "__main__":
    DBtest = download_DB()
    for x in DBtest:
        print(x)
    print(type(DBtest))