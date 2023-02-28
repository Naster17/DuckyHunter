import os
import core
import time
from config import *

def Convert(letter):
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

def DEFAULTDELAY(line):
    milis = int(data) / 1000
    return milis


def STRING(line, default_write_delay):

    for letter in line:
        time.sleep(default_write_delay)
        if letter.isupper():
            print(
                f'echo "left-shift {letter.lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
        elif letter.islower():
            print(
                f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
        elif letter.isnumeric():
            print(
                f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')
        else:
            symbol = Convert(letter)
            print(
                f'echo "{symbol}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{symbol}" | ./hid-keyboard {self.hid} {self.hid_type} > /dev/null')

