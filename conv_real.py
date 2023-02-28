import os
import time
import json

# wewe

class Converter:
    def __init__(self):
        # self.cmd_list = ["REM", "DELAY", "GUI", "ENTER", "DEFAULTDELAY", "DEFAULT_DELAY", "STRING"]
        self.hid = "/dev/hidg0"
        self.hid_type = "keyboard"
        self.default_delay = 0.01

    ########################
    #       Analyzer       #
    ########################
    def Analyze(self, file):
        with open(file) as f:
            for line in f:
                line = line.strip().split()
                try:
                    self.Executer(line)
                    time.sleep(self.default_delay)
                except:
                    print(f"Unsupported command: {line} ")
                    pass
    
    ########################
    #       Executer       #
    ########################
    def Executer(self, line):
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
            os.popen(f'echo "enter" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')

        elif line[0] == "GUI":
            try:
                if line[1] != None:
                    print(f'echo "left-meta {line[1]}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    os.popen(f'echo "left-meta {line[1]}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
            except:
                print(f'echo "left-meta" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                os.popen(f'echo "left-meta" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')

        elif line[0] == "STRING":
            line = " ".join(line[1:])
            for letter in line:
                time.sleep(0.01)
                if letter.isupper():
                    print(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    os.popen(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                elif letter.islower():
                    print(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                elif letter.isnumeric():
                    print(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                else:
                    symbol = self.Convert(letter)
                    print(f'echo "{symbol}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
                    os.popen(f'echo "{symbol}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
        
        else:
            print(f"Unsupported command: {' '.join(line)}")
        
    
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
            


            
        
        

    
            
Converter().Analyze("script.txt")