
from calculator import Calculate
from tools import Tools

import ui

def run(path, standard):
	try:
		path = path.get()
		with open(path, "r") as handler:
			string = handler.read()
	except Exception as error:
		ui.open_fail()
		return

	try:
		standard = int(standard.get())
	except ValueError as error:
		ui.invalid_value()
		return

	datas = Tools.spliter(string)
	instance = Calculate(standard, datas)

	table = '\n'.join([
		Tools.title(),
		Tools.table(instance.iterators()) + '\n',
		Tools.annotation(**instance.information())
	])
	Tools.drawtable(table)

	axis = instance.axis()
	normal = instance.normal()

	Tools.drawline(axis)

	instance.reset()
	Tools.drawbar(axis, normal)

	ui.success()
	return

if __name__ == "__main__":
	ui.init(run)
	ui.root.mainloop()
