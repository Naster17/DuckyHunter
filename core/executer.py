import os
import time
import json

import core.functions as cmd
import core.android_api as android_api
from config import *

class Core:
    def __init__(self):
        self.universal_keys = ["UP", "DOWN", "LEFT", "RIGHT", "ENTER",
                               "PAGEUP", "PAGEDOWN", "END", "HOME",
                               "ESC", "INSERT", "SPACE", "TAB", "PRINTSCREEN", "SHIFT", "ALT", "CTRL", "BACKSPACE","DELETE",
                               "NUMLOCK", "SCROLLOCK","SCROLLLOCK", "CAPSLOCK",
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
        time.sleep(default_delay)
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
                cmd.STRING(line)

            elif line[0] == "STRINGLN":
                cmd.STRINGLN(line)

            elif line[0] == "LED_ON":
                print("LED_ON")
                android_api.LED_ON()

            elif line[0] == "LED_OFF":
                print("LED_OFF")
                android_api.LED_OFF()

            elif line[0] == "LEDF_ON":
                print("LEDF_ON")
                android_api.LEDF_ON()
            elif line[0] == "LEDF_OFF":
                print("LEDF_OFF")
                android_api.LEDF_OFF()
            
            elif line[0] == "IF_PLUGGED":
                android_api.IF_PLUGGED()
            
            elif line[0] == "IF_UNPLUGGED":
                android_api.IF_UNPLUGGED()

            
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
