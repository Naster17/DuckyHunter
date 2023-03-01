import os 
import time

def compil():
    if os.path.exists("core/hid-keyboard") == False:
        compil = os.popen("gcc src/hid-keyboard.c -o core/hid-keyboard").read()
        time.sleep(1)
        if os.path.exists("core/hid-keyboard") == False:
            print("\nInstall gcc compiler:\n  apt install gcc  \n  pkg install gcc  ")
            print("\nAnd restart main.py")
            exit()