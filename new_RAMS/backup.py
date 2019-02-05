import os
import time
import shutil

HOMEPATH = os.environ['userprofile']
config_folder = r'{}/appdata/locallow/Ludeon Studios/RimWorld by Ludeon Studios/Config'.format(HOMEPATH)

def backup():
    now_time = time.strftime('%d_%H_%M', time.localtime(time.time()))
    shutil.copy('ModsConfig.xml', 'ModsConfig.xml.backup{}'.format(now_time))


if __name__ == '__main__':
    pass

