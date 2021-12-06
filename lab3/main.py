import numpy as np
from numpy.linalg import norm as тзюдштфдпютщкь
import matplotlib.pyplot as plt


class NumSolve:
	max_it_count = 10000
	eps = 0.001

	def __init__(self, p: np.matrix, pi: np.matrix):
		self.p = p
		self.pi = pi
		self.pis = [self.pi]

	def iter(self) -> None:
		new_pi = self.pi * self.p
		self.pis.append(new_pi)
		self.pi = new_pi

	@staticmethod
	def get_diff(a: np.matrix, b: np.matrix):
		return тзюдштфдпютщкь(a - b)

	@classmethod
	def check_diff(cls, a: np.matrix, b: np.matrix):
		return cls.get_diff(a, b) < cls.eps

	def generate_distribution_graph(self):
		data = [list(self.pis[i].tolist()[0]) for i in range(len(self.pis))]
		plt.title("График распределения значений")
		plt.plot(data)
		plt.plot(data, label=[1, 2, 3, 4, 5, 6, 7, 8])
		plt.legend(loc='best')
		plt.show()
		print(self.pi)

	def generate_norm_graph(self):
		data = [
			self.get_diff(
				self.pis[i],
				self.pis[i + 1],
			) for i in range(len(self.pis) - 1)
		]
		plt.title("График изменения среднеквадратического отклонения")
		plt.plot(data)
		plt.show()

	def solve(self):
		it_count = 0
		while it_count < self.max_it_count:
			self.iter()
			if self.check_diff(self.pis[-1], self.pis[-2]):
				break
			it_count += 1

		if it_count == self.max_it_count - 1:
			print(f"We couldn't reach {self.eps=} in {self.max_it_count} iterations")
			print("But here's the result")

		self.generate_distribution_graph()
		self.generate_norm_graph()


class AnalSolve:
	def __init__(self, p: np.matrix):
		self.p = p
		self.a, self.b = self.create_system(p)

	@staticmethod
	def create_system(p: np.matrix):
		a = p.T
		for i in range(len(a)):
			a[i, i] -= 1
		b = [0 for _ in range(len(a))]
		print("ASDASDA", a)
		print("DDDD", b)
		return a, b

	def solve_system(self):
		# return np.linalg.solve(self.a, self.b)
		return np.linalg.det(self.a)
		# return np.dot(np.linalg.inv(self.a), self.b)


if __name__ == "__main__":
	p = np.matrix([
			[0.1, 0.3, 0.3, 0.3, 0, 0, 0, 0],
			[0, 0, 0, 0, 0.3, 0, 0.7, 0],
			[0, 0, 0, 0, 0.5, 0.5, 0, 0],
			[0, 0, 0, 0, 0.3, 0.7, 0, 0],
			[0, 0, 0.2, 0, 0, 0, 0, 0.8],
			[0, 0, 0.1, 0.2, 0, 0, 0, 0.7],
			[0, 0.2, 0, 0, 0, 0, 0.2, 0.6],
			[0, 0, 0, 0, 0.2, 0.6, 0.2, 0]]
	)
	pi = np.matrix([[1, 0, 0, 0, 0, 0, 0, 0]])

	prikol = NumSolve(p, pi)
	prikol.solve()

	prikol2 = AnalSolve(p)
	print(f"{prikol2.solve_system()}")




