import time 
import os

from core.executer import Core
from config import *
from core.compiler import compil

# Simple compiler
compil()


hid = Core() 
hid.Analyzer("script.txt")
