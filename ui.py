"""Draw a GUI using TK"""

from consts import *

def _exit():
	root.destroy()
	sys.exit()

_select = lambda : _PATH.set(askopenfilename())
open_fail = lambda: msgbox.showerror("Error", "Open file error!")
invalid_value = lambda: msgbox.showerror("Error", "Invalid standard value!")
success = lambda: msgbox.showinfo("Success", "Analysis completed! \nNow exiting...")

def notepad(file):
	program = "notepad " if os.name == "nt" else "vi"
	os.popen(program + file, "r")
_help = lambda : notepad(HELP)

_title = "Data Analyser"

_resizableX = False
_resizableY = False

root = Tk()

_PATH = StringVar()
_STANDARD = StringVar()

def init(function):
	"""Initalize UI"""

	_menubar = Menu(root)
	_menubar.add_command(label = "Select Data File", command = _select)
	_menubar.add_command(label = "Help", command = _help)
	_menubar.add_command(label = "Exit", command = _exit)

	_label_file = Label(root, text = "Datafile location: ")
	_label_file.grid(row = 0, column = 0, pady = 10)

	_choose_entry = Entry(root, textvariable = _PATH)
	_choose_entry.grid(row = 0, column = 1, padx = 10)

	_label_standard = Label(root, text = "Standard value: ")
	_label_standard.grid(row = 1, column = 0)

	_standard_entry = Entry(root, textvariable = _STANDARD)
	_standard_entry.grid(row = 1, column = 1)

	_run_btn = Button(root, text = "Generate",
		command = lambda: function(_PATH, _STANDARD))
	_run_btn.grid(row = 2, column = 0, columnspan = 2, pady = 10)

	root.resizable(_resizableX, _resizableY)
	root.config(menu = _menubar)
	root.geometry('330x120')
	root.title(_title)
