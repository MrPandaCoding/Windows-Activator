import os
from os import system
import time
import ctypes, sys


x = "Windows Activator By: Noah W."
system("title " + x)

print("hello")

print("=====================================================""\n#Project: Activation of Windows Software products.\n""=====================================================\n")
print("#Supported products:\n""- Windows 10 Home\n- Windows 10 Professional\n")
print("=====================================================")
time.sleep(1.5)
print("Activating Windows...")
time.sleep(1.5)
print("please wait...")
time.sleep(0.5)
print("=====================================================")
time.sleep(0.8)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():

    os.system('cmd /c "slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"')
    os.system('cmd /c "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"')
    os.system('cmd /c "slmgr /skms s7.uk.to"')
    os.system('cmd /c "slmgr /skms s8.uk.to"')
    os.system('cmd /c "slmgr /skms s9.uk.to"')
    os.system('cmd /c "slmgr /ato"')
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)