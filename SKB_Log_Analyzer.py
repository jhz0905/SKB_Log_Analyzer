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

# Check Hostname #
    if os_name == "Cisco IOS XR Software":
        for host_parsing in range(len(log_line)):
            host_pattern = r'^\w\w/\d/\w+\d/\w\w\w\d:.*#show'
            host_result = re.search(host_pattern, log_line[host_parsing])
            if host_result != None:
                hostname = host_result.group()
                hostname = hostname.split(sep = ":", maxsplit = 1)
                hostname = hostname[1]
                hostname = hostname.split(sep = "#", maxsplit = 1)
                hostname = hostname[0]
                break
            else:
                pass

        for hw_parsing in range (len(log_line)):
            hw_pattern = r'^ASR \d{1,4} \d{1,2} Line Card Slot Chassis'
            hw_result = re.search(hw_pattern, log_line[hw_parsing])
            if hw_result != None:
                hw_result = hw_result.group()
                hw_pattern2 = r'^ASR \d{1,4}'
                hw_result2 = re.search(hw_pattern2, log_line[hw_parsing])
                hw_result2 = hw_result2.group()
                hw_type = hw_result2
                break
            else:
                pass

        if os.path.exists("%s\%s.txt" %(str(nextdir),hostname)) == True:
            if file_list[file_num] != "%s.txt" %hostname:
                os.remove("%s\%s" %(str(nextdir),file_list[file_num]))
                print("####### remove %s(%s) #######" %(hostname, file_list[file_num]))
        else:
            os.rename("%s" %file_list[file_num],"%s.txt" %hostname)
        #print("Filename %s -> %s.txt" %(file_list[file_num], hostname))

    else:
        for host_parsing in range(len(log_line)):
            host_pattern = r'^.*#show version$'
            host_result = re.search(host_pattern, log_line[host_parsing])
            if host_result != None:
                hostname = host_result.group()
                hostname = hostname.split(sep = "#s", maxsplit = 1)
                hostname = hostname[0]
                break
            else:
                pass

        if os.path.exists("%s\%s.txt" %(str(nextdir),hostname)) == True:
            if file_list[file_num] != "%s.txt" %hostname:
                os.remove("%s\%s" %(str(nextdir),file_list[file_num]))
                print("####### remove %s(%s) #######" %(hostname, file_list[file_num]))
        else:
            os.rename("%s" %file_list[file_num],"%s.txt" %hostname)
        #print("Filename %s -> %s.txt" %(file_list[file_num], hostname))

        for hw_parsing in range(len(log_line)):
            hw_pattern = r'^PID:\s.*\s*.*$'
            hw_result = re.search(hw_pattern, log_line[hw_parsing])
            if hw_result != None:
                hw_type = hw_result.group()
                hw_type = hw_type.split(sep = " ", maxsplit = 2)
                hw_type = hw_type[1]
                break
            else:
                pass

