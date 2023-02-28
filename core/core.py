import os
import time
import json

import core.android_api as android_api

class Converter:
    def __init__(self):
        self.led = "/sys/class/leds/red/brightness"
        self.ledf = "/sys/class/leds/flashlight/brightness"
        self.hid = "/dev/hidg0"
        self.hid_type = "keyboard"
        self.default_delay = 0.01
        self.default_write_delay = 0.02

    ########################
    #       Analyzer       #
    ########################
    def Analyzer(self, file):
        with open(file) as f:
            for line in f:
                line = line.strip().split()
                try:
                    self.Executer(line)
                except:
                    print(f"Unsupported command: {line} ")
                    pass
    
    ########################
    #       Executer       #
    ########################
    def Executer(self, line):
        time.sleep(self.default_delay)
        
        if line[0] in ["DEFAULTDELAY", "DEFAULT_DELAY"]:
            milis = int(line[1]) / 1000
            self.default_delay = milis
            print(f"DEFAULTDELAY: {line[1]}")

        elif line[0] == "REM":
            print("### " + " ".join(line[1:]) + " ###")

        elif line[0] == "DELAY":
            milis = int(line[1]) / 1000
            print(f"SLEEPING {milis} secs.")
            time.sleep(milis)
        
        elif line[0] == "ENTER":
            print(f'echo "enter" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
            # os.popen(f'echo "enter" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')

    

        elif line[0] == "GUI":
            try:
                if line[1] != None:
                    print(f'echo "left-meta {line[1]}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    # os.popen(f'echo "left-meta {line[1]}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
            except:
                print(f'echo "left-meta" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                # os.popen(f'echo "left-meta" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')

        elif line[0] == "STRING":
            line = " ".join(line[1:])
            for letter in line:
                time.sleep(self.default_write_delay)
                if letter.isupper():
                    print(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    # os.popen(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                elif letter.islower():
                    print(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    # os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                elif letter.isnumeric():
                    print(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    # os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                else:
                    symbol = self.Convert(letter)
                    print(f'echo "{symbol}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    # os.popen(f'echo "{symbol}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
        
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
        
    #########################
    #    Layout Converter   #
    #########################
    def Convert(self, letter):
        letter = str(letter)
        with open('layouts/us.json') as f:
            data = json.load(f)
            symbols = data["SYMBOLS"]
            special = data["SPECIAL"]

            if letter in symbols:
                value = symbols[letter]
                return value
            elif letter in special:
                value = special[letter]
                return value
            
        