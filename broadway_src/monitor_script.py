import csv
from datetime import datetime
from email import message
import os
import subprocess
import sys
import time
from turtle import home

# define working directory tree & PARANS

NUM_OF_PROCESSES_TO_MONITOR = 0 # how many processes to return in STOUT - default 0

home_dir = os.getcwd()
monitoring_path = "monitoring"
top_filename_stout = "top_process_output"
monitoring_status_file_name = "monitoring_status"

monitoring_path = os.path.join(home_dir, monitoring_path)
if not os.path.exists(monitoring_path):
    os.mkdir(monitoring_path)

header = ['date', 'message']
monitoring_file_obj = open(f"{os.path.join(monitoring_path, monitoring_status_file_name)}.csv", "w", encoding='UTF8', newline='')

def run_top_process():
    with open(f"{os.path.join(monitoring_path, top_filename_stout)}.csv", "w", encoding='UTF8', newline='') as output_file:
    #p = subprocess.Popen("top -n 0", stdout=subprocess.PIPE, shell=True)
        
        message_on_success = "top porcess is running"
        message_on_fail = "top command did NOT run"
        writer = csv.writer(monitoring_file_obj, quoting=csv.QUOTE_ALL, delimiter=';')
        try:
            #subprocess.call(f"top -n {NUM_OF_PROCESSES_TO_MONITOR}", shell=True, stdout=output_file)
            subprocess.call(f"ps -ef | grep top | grep -v grep", shell=True)
            writer.writerow([datetime.now().strftime("%m/%d/%Y, %H:%M:%S") ,message_on_success])
        except Exception as e:
            writer.writerow([str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) ,message_on_fail])
            print(e) # could also return value to indicate on error for progressed monitoring tool.

# main process of python
if __name__ == "__main__":
    # there could many different tools that already provide monitoring base lines.
    # in this script i am:
    # running a proc with endless loop to run it iteratevly, i am aware that it could break.
    # we can overcome it  with several ways - 2 for example:
    # 1. to host it on webserver and in any case of failing to restart it again
    # 2. icinga and so on..
    
    try:
        while True:
            run_top_process()
            time.sleep(1)
    except Exception as e:
        print(f"error occured in monitoring script, error message: {e}")