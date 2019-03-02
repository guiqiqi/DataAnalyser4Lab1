"""Package source code to single exe file"""

import cx_Freeze
import sys
import traceback

base = None

if sys.platform == "win32":
	base = "Win32GUI"

executables = [
	cx_Freeze.Executable(
		"main.pyw", base = base
	)
]

cx_Freeze.setup(
	name = "DataAnalyser4Lab1",
	options = {
		# "include_files": ["help"],
		# "optimize": 2,
		"build_exe": {
			"packages": [
				"matplotlib.pyplot",
				"tkinter.filedialog",
				"tkinter.ttk",
				"tkinter",
				"math", "os"
			]
		}
	},
	version = "0.0.1",
	description = "Data analysis program for PE1",
	executables = executables,
	author = "guiqiqi187@gmail.com"
)
