import os
import time
import json

import core.functions as cmd
import core.android_api as android_api
from config import *

class Core:
    def __init__(self):
        self.led = led
        self.ledf = ledf
        self.hid = hid
        self.hid_type = hid_type
        self.default_delay = default_delay
        self.default_write_delay = default_write_delay
        self.universal_keys = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER", "CAPSLOCK", "PAGEUP", "PAGEDOWN", "DELETE", "END", "HOME",
                                "INSERT", "NUMLOCK", "SCROLLOCK","SCROLLOCK", "SPACE", "TAB", "PRINTSCREEN", "SHIFT", "ALT", "CTRL",
                                 "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]

    def Analyzer(self, file):
        with open(file) as f:
            for line in f:
                line = line.strip().split()
                # try:
                self.Executer(line)
                # except:
                #     print(f"Unsupported command: {line} ")
                #     pass

    def Executer(self, line):
        time.sleep(self.default_delay)
        try:
            if line[0] in ["DEFAULTDELAY", "DEFAULT_DELAY"]:
                self.default_delay = cmd.DEFAULTDELAY(line)
                
            elif line[0] == "REM":
                cmd.REM(line)

            elif line[0] == "DELAY":
                cmd.DELAY(line)

            elif line[0] == "GUI":
                cmd.GUI(line)

            elif line[0] == "STRING":
                cmd.STRING(line, self.default_write_delay)

            elif line[0] == "STRINGLN":
                cmd.STRINGLN(line, self.default_write_delay)

            elif line[0] == "LED_ON":
                print("LED_ON")
                android_api.LED_ON(self.led)

            elif line[0] == "LED_OFF":
                print("LED_OFF")
                android_api.LED_OFF(self.led)

            elif line[0] == "LEDF_ON":
                print("LEDF_ON")
                android_api.LEDF_ON(self.ledf)
            elif line[0] == "LEDF_OFF":
                print("LEDF_OFF")
                android_api.LEDF_OFF(self.ledf)

            
            elif line[0] in ["UPARROW", "DOWNARROW", "LEFTARROW", "RIGHTARROW"]:
                cmd.ONLY_ARROW(line)
            
            elif line[0] in self.universal_keys:
                cmd.UNIVERSAL(line)


            else:
                print(f"Unsupported command while: {' '.join(line)}, {line}")

        except IndexError:
            # In case there are empty lines in the script
            # This will help it continue if there is something after the lines
            # And you can create more readable syntax
            pass
