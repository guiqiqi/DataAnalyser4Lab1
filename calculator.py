"""Iterator and general calc functions support"""

from consts import *

class Calculate(object):
	"""Calculate constant for datas"""
	def __init__(self, standard, datas):
		"""init for iterators"""
		self.standard = standard
		self.datas = datas

	def reset(self):
		new_iterator = Calculate(self.standard, self.datas)
		self = new_iterator

	def information(self):
		return {
			"max": max(self.datas),
			"min": min(self.datas),
			"range": self.range(),
			"average": self.average(),
			"sigma": self.sigma()
		}

	def index(self):
		for index in range(1, len(self.datas) + 1):
			yield index
		return

	def data(self):
		for item in self.datas:
			yield item
		return

	def difference(self):
		for item in self.datas:
			yield self.round(item - self.standard)
		return

	def variance(self):
		for item in self.datas:
			yield self.round((item - self.standard) ** 2)
		return

	def rho(self):
		sigma = self.sigma()
		average = self.average()
		for data in self.datas:
			yield self.round(self._rho(sigma, average, data))
		return

	def iterators(self):
		return [
			self.index(),
			self.data(),
			self.difference(), 
			self.variance(), 
			self.rho()
		]

	def average(self):
		return sum(self.datas)/len(self.datas)

	def range(self):
		return self.round(max(self.datas) - min(self.datas))

	def sigma(self):
		sum_variance = sum(self.variance())
		return math.sqrt(sum_variance / len(self.datas))

	def linspace(self, segment = SEGMENT):
		axis = dict()
		_max, _min = max(self.datas), min(self.datas)
		length = _max - _min
		splice = length / segment
		while _min < _max:
			start, end = _min, self.round(_min + splice)
			axis[(start, end)] = list()
			_min = end
		for data in self.datas:
			for interval in axis.keys():
				start, end = interval
				if start <= data <= end:
					axis[interval].append(data)
		return axis

	def axis(self):
		line = self.linspace()
		return {key: len(datas) for key, datas in line.items()}

	@staticmethod
	def round(number, accuracy = ACCURACY):
		return (round(number * accuracy) / accuracy)

	@staticmethod
	def _rho(sigma, average, data):
		_upi = 1 / (math.sqrt(2 * math.pi))
		exponent = -1 * \
		(data - average) ** 2 / (2 * sigma ** 2)
		return (_upi / sigma) * (math.e ** exponent)
