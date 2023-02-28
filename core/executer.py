import os
import time
import json
import core.functions as cmd

import core.android_api as android_api


class Core:
    def __init__(self, led, ledf, hid, hid_type):
        self.led = led
        self.ledf = ledf
        self.hid = hid
        self.hid_type = hid_type
        # DELAY times
        self.default_delay = 0.01
        self.default_write_delay = 0.02

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

            elif line[0] == "ENTER":
                cmd.ENTER()

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

            else:
                print(f"Unsupported command while: {' '.join(line)}")

        except IndexError:
            # In case there are empty lines in the script
            # This will help it continue if there is something after the lines
            # And you can create more readable syntax
            pass
