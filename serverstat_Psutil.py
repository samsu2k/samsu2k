import os
import psutil as PSUTIL
import time
while True:

    with open('yourfilelocation', "a") as myfile:
        myfile.write(str(PSUTIL.cpu_percent(interval=1)) + os.linesep)
    time.sleep(60)
