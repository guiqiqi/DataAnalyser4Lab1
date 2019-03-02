"""Text I/O functions"""

from consts import *

class Tools(object):
	def drawtable(table):
		with open(TABLE, "w") as handler:
			handler.write(table)

	def drawbar(axis, datas, rho):
		# Prepare for datas
		x, y = list(), list()
		for splice, value in axis.items():
			calc_x = (splice[0] + splice[1]) / 2
			x.append(round(calc_x, 3))
			y.append(value)

		# Draw the bar
		figure = plt.figure(dpi = 360, facecolor = "white")
		axes = plt.subplot(111)
		axes.bar(x, y, width = 0.1)
		axes.set_xticks(x)
		axes.set_yticks(y)

		plt.savefig(BAR)

	def drawline(axis):
		# Prepare for datas
		x, y = list(), [0] * (SEGMENT + 1)
		for splice in axis.keys():
			x.extend(splice)
		x = list(set(x)); x.sort()
		offset = (max(x) - min(x)) / (SEGMENT * 2)

		# Draw the axis
		figure = plt.figure(dpi = 360, facecolor = "white")
		axes = plt.subplot(111)
		axes.plot(x, y, color = "black", linewidth = 0)
		axes.spines['right'].set_color('none')
		axes.spines['top'].set_color('none')
		axes.spines['bottom'].set_position(('data',0))
		axes.spines['left'].set_position(('data',0))
		axes.set_xticks(x)
		axes.set_yticks([])
		axes.set_ylim(-0.5, 0.5)
		for position, count in axis.items():
			x_position = position[0]
			axes.text(x_position + offset, 0.05, count, size = 10)

		plt.savefig(AXIS)

	def spliter(string):
		string = string.strip()
		string = string.replace('\n', ' ')
		substrings = string.split(' ')
		datas = [float(item) for item in substrings]
		return datas 

	def annotation(**annotations):
		result = list()
		model = "**{key} = {value}"
		for key, value in annotations.items():
			result.append(model.format(
				key = key, value = value))
		return '\n'.join(result)

	def title():
		titler = list()
		titles = ["No.", "t", "t-<t>", "(t-<t>)^2", "rho"]
		divider = '-' * WIDTH * len(titles)
		for title in titles:
			titler.append(title.center(WIDTH))
		return ''.join(titler) + '\n' + divider

	def table(iterators):
		_flag = True
		result = list()
		while _flag:
			for iterator in iterators:
				try:
					data = next(iterator)
				except StopIteration as _error:
					_flag = False
					break
				result.append(str(data).center(WIDTH))
			result.append('\n')
		return ''.join(result).strip('\n')
