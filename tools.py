"""Text I/O functions"""

from consts import *

class Tools(object):
	def drawtable(table):
		with open(TABLE, "w") as handler:
			handler.write(table)

	def drawbar(axis, normal):
		# Prepare for datas
		_sum = sum(axis.values())
		xtick = set()
		x, y = list(), list()
		for splice, value in axis.items():
			gap = splice[1] - splice[0]
			xtick.add(splice[0])
			xtick.add(splice[1])
			x.append((splice[0] + splice[1]) / 2)
			y.append(value / gap / _sum)
		xtick = list(xtick); xtick.sort()
		figure, axes = plt.subplots(dpi = 360, facecolor = "white")

		# Draw the bar
		axes_bar = axes
		axes_bar.bar(x, y, width = gap,
			facecolor = "blue", edgecolor = "yellow",
			linestyle = '--', linewidth = 1, alpha = 0.6)
		axes_bar.set_xticks(xtick)

		# Add data annotations
		for position, value in zip(x, y):
			plt.text(position, value + 0.02, "%.2f" % value,
				ha = "center", va = "bottom", fontsize = 7)

		# Draw thee normal distribution
		axes_normal = axes.twinx()
		axes_normal.scatter(normal.keys(), normal.values(),
			color = "red", alpha = 0.5)
		# axes_normal.set_yticks([])

		plt.ylim(0, max(y) + 0.3)
		# plt.show()
		plt.savefig(BAR)
		plt.close(figure)

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

		# plt.show()
		plt.savefig(AXIS)
		plt.close(figure)

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
		titles = ["No.", "t", "t-<t>", "(t-<t>)^2"]
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
