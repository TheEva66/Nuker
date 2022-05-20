import subprocess
import time
import os
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
f= open("HWID.txt","w+")
f.write(hwid)
f.close
print("HWID printed to HWID.txt")
time.sleep(10)
