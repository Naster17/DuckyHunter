import os
import core
import time
import json
from config import *

def Convert(letter):
    with open('layouts/us.json') as f:
        data = json.load(f)
        
        symbols = data["SYMBOLS"]
        special = data["SPECIAL"]

        if type(letter) == str:
            if letter in symbols:
                return symbols[letter]
                
            elif letter in special:
                return special[letter]
     


        f.close()


def UNIVERSAL(line):

    print(f'echo "{" ".join(line).lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    os.popen(f'echo "{" ".join(line).lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
 

     

def MODIFIER(line):
    print(line)

def DEFAULTDELAY(line):
    print(f"DEFAULTDELAY: {line[1]}")
    milis = int(line[1]) / 1000
    return milis

def REM(line):
    print("### " + " ".join(line[1:]) + " ###")

def ENTER():
    print(f'echo "enter" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    os.popen(f'echo "enter" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    

def DELAY(line):
    milis = int(line[1]) / 1000
    print(f"DELAY {line[1]}")
    time.sleep(milis)

def GUI(line):
    try:
        if line[1] != None:
            print(f'echo "gui {line[1]}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "gui {line[1]}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    except:
        print(f'echo "gui" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        os.popen(f'echo "gui" | ./{path_to_hid} {hid} {hid_type} > /dev/null')

def STRING(line):
    line = " ".join(line[1:])
    for letter in line:
        time.sleep(default_write_delay)
        

        if letter.isupper():
            print(f'echo "left-shift {letter.lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "left-shift {letter.lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        elif letter.islower():
            print(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        elif letter.isnumeric():
            print(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        else:
            symbol = Convert(letter)
            print(f'echo "{symbol}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{symbol}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')

def STRINGLN(line):
    line = " ".join(line[1:])
    for letter in line:
        time.sleep(default_write_delay)
        
        if letter.isupper():
            print(
                f'echo "left-shift {letter.lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "left-shift {letter.lower()}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        elif letter.islower():
            print(
                f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        elif letter.isnumeric():
            print(
                f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{letter}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        else:
            symbol = Convert(letter)
            print(
                f'echo "{symbol}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
            os.popen(f'echo "{symbol}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')

    print(f'echo "enter" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    os.popen(f'echo "enter" | ./{path_to_hid} {hid} {hid_type} > /dev/null')

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
                print(f'echo "{line}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
                os.popen(f'echo "{line}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
                a += 1
                if a == line:
                    break
     
    except:
        print(f'echo "{line}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
        os.popen(f'echo "{line}" | ./{path_to_hid} {hid} {hid_type} > /dev/null')


def PRINTSCREEN():
    print(f'echo "print" | ./{path_to_hid} {hid} {hid_type} > /dev/null')
    os.popen(f'echo "print" | ./{path_to_hid} {hid} {hid_type} > /dev/null') 