import time
import os
import argparse

from core.executer import Core
from config import *
from core.compiler import compil

compil()

print("""       ,~~.
      (  6 )-_,
 (\___ )=='-'
  \ .   ) )     DuckyHunter Beta Edition
   \ `-' /    
~'`~'`~'`~'`~""")

parser = argparse.ArgumentParser(description="")

parser.add_argument('--file', type=str, help='Path to script')

args = parser.parse_args()



hid = Core()
try:
    hid.Analyzer(args.file)
except TypeError:
    print("usage: main.py [-h] [--file FILE]")
except FileNotFoundError:
    print("\nQUACK!!! ")
    print(f"File {args.file} not found")
