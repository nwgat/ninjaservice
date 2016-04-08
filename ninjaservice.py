# nwgat.ninja
import os
import subprocess
import schedule
import arrow
from time import sleep

def job():
    utc = arrow.utcnow()
    output = subprocess.check_output(["ps", "x"]);  # linux
#   output = subprocess.check_output(["tasklist"]); # windows
    if "lftp\b" in output:
         print 'lftp is already running'
    else:
         cmd = 'lftp -f /home/user/script' # linux
#         cmd = 'bash.exe -c "/usr/bin/lftp.exe -f /cygdrive/d/sb/bin/tv.lftp"' #windows
         os.system(cmd)

#schedule.every(9).seconds.do(job)
schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    sleep(1)
