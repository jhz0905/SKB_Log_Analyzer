import os
import re
from openpyxl import load_workbook

print("### Wait.. Inspection Ongoing ###")
nowdir = os.getcwd()
logdir = "\log"
nextdir = nowdir+logdir
os.chdir(str(nextdir))

# Parsing #

for file_num in range(len(file_list)):

# Constant #
    os_name = 0
    hostname = 0
    hw_type = 0

# Read a Log # 
    log_file = open("%s" %file_list[file_num], "r")
    log_line = log_file.readlines()
    log_file.close()

# Check OS #
    for os_parsing in range(len(log_line)):
        os_pattern = r'^Cisco\s(IOS|Internetwork Operating System|IOS XR)\sSoftware'
        os_result = re.search(os_pattern, log_line[os_parsing])
        if os_result != None:
            os_name = os_result.group()
            break
        else:
            pass