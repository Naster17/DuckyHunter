import os
from config import *

def LED_ON(led):
    os.popen(f"echo 254 > {led}")
    pass
def LED_OFF(led):
    os.popen(f"echo 0 > {led}")
    pass
def LEDF_ON(ledf):
    os.popen(f"echo 254 > {ledf}")
    pass
def LEDF_OFF(ledf):
    os.popen(f"echo 0 > {ledf}")
    pass

