import os
import time
from config import *


def LED_ON():
    os.popen(f"echo 254 > {led}")
    pass


def LED_OFF():
    os.popen(f"echo 0 > {led}")
    pass


def LEDF_ON():
    os.popen(f"echo 254 > {ledf}")
    pass


def LEDF_OFF():
    os.popen(f"echo 0 > {ledf}")
    pass


def IF_PLUGGED():
    while 1:
        status = os.popen(f"cat {usb}").read().strip()

        if status == "1":
            break
        elif status == "0":
            time.sleep(check_sleep_time)
        

def IF_UNPLUGGED():
    while 1:
        status = os.popen(f"cat {usb}").read().strip()

        if status == "0":
            break
        elif status == "1":
            time.sleep(check_sleep_time)