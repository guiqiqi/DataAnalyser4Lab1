"""Define consts"""

import math
import matplotlib.pyplot as plt

from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter.messagebox as msgbox
from tkinter.ttk import *

import os

ACCURACY = 10000 # default accuracy is 10**-5
WIDTH = 12 # default width for every table column
SEGMENT = 7 # default segments for operator linspace

AXIS = "axis.png" # default axis figure filename
BAR = "bar.png" # default bar figure filename
TABLE = "table.txt" # default table filename

HELP = "help" # Help file
