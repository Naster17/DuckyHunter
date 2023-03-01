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
        universal = data["UNIVERSAL"]

        if letter in symbols:
            value = symbols[letter]
            return value
        elif letter in special:
            value = special[letter]
            return value
        elif letter in universal:
            value = universal
            return value


def UNIVERSAL(line):
    low_line = str(line[0]).lower()

    if len(line) >= 2:
        print(f'echo "{" ".join(line).lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        # os.popen(f'echo "{" ".join(line).lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    else:
        print(f'echo "{low_line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        # os.popen(f'echo "{low_line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')    

     



def MODIFIER(line):
    print(line)

def DEFAULTDELAY(line):
    print(f"DEFAULTDELAY: {line[1]}")
    milis = int(line[1]) / 1000
    return milis

def REM(line):
    print("### " + " ".join(line[1:]) + " ###")

def ENTER():
    print(f'echo "enter" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    # os.popen(f'echo "enter" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    

def DELAY(line):
    milis = int(line[1]) / 1000
    print(f"DELAY {line[1]}")
    time.sleep(milis)

def GUI(line):
    try:
        if line[1] != None:
            print(f'echo "left-meta {line[1]}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "left-meta {line[1]}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    except:
        print(f'echo "left-meta" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        # os.popen(f'echo "left-meta" | ./hid-keyboard {hid} {hid_type} > /dev/null')

def STRING(line, default_write_delay):
    line = " ".join(line[1:])
    for letter in line:
        time.sleep(default_write_delay)

        if letter.isupper():
            print(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        elif letter.islower():
            print(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        elif letter.isnumeric():
            print(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        else:
            symbol = Convert(letter)
            print(f'echo "{symbol}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{symbol}" | ./hid-keyboard {hid} {hid_type} > /dev/null')

def STRINGLN(line, default_write_delay):
    line = " ".join(line[1:])
    for letter in line:
        time.sleep(default_write_delay)
        
        if letter.isupper():
            print(
                f'echo "left-shift {letter.lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "left-shift {letter.lower()}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        elif letter.islower():
            print(
                f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        elif letter.isnumeric():
            print(
                f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{letter}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        else:
            symbol = Convert(letter)
            print(
                f'echo "{symbol}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
            # os.popen(f'echo "{symbol}" | ./hid-keyboard {hid} {hid_type} > /dev/null')

    print(f'echo "enter" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    # os.popen(f'echo "enter" | ./hid-keyboard {hid} {hid_type} > /dev/null')

def ONLY_ARROW(line):

    if line[0] == "UPARROW":
        line = "up"
    elif line[0] == "DOWNARROW":
        line = "down"
    elif line[0] == "LEFTARROW":
        line = "left"
    elif line[0] == "RIGHTARROW":
        line = "right"

    try:
        if line[1] != None:
            a = 0
            line = int(line[1])
            while True:
                print(f'echo "{line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
                # os.popen(f'echo "{line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
                a += 1
                if a == line:
                    break
     
    except:
        print(f'echo "{line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')
        # os.popen(f'echo "{line}" | ./hid-keyboard {hid} {hid_type} > /dev/null')


def PRINTSCREEN():
   print(f'echo "print" | ./hid-keyboard {hid} {hid_type} > /dev/null')
    # os.popen(f'echo "{line}" | ./hid-keyboard {hid} {hid_type} > /dev/null') 