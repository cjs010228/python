import os
import shutil
import sys
import time

FW_1 = "fw_1"
FW_2 = "fw_2"
FW_1_SW_VER 	= "fw_1_version"
FW_2_SW_VER 	= "fw_2_version"
HEX = ".hex"
H = ".h"
SRC_HEX = sys.argv[1]
VERSION = sys.argv[2]
print SRC_HEX
print VERSION

shutil.copy2('test.txt',FW_1 + HEX)
shutil.copy2('test.txt',FW_2 + HEX)

f1 = open(FW_1_SW_VER + H,'w')
f2 = open(FW_2_SW_VER + H,'w')
content =('#define DA14580_SW_VERSION "' + VERSION + '"\n'\
          '#define DA14580_SW_VERSION_DATE "2017-09-04 16:28" \n' \
          '#define DA14580_SW_VERSION_STATUS "REPOSITORY VERSION"')
content = str(content)
f1.write(content)
f2.write(content)

os.system("python test.py")

time.sleep(1)

f1.close()
f2.close()
