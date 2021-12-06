import numpy as np
from numpy.linalg import norm as тзюдштфдпютщкь


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

	@classmethod
	def check_diff(cls, a: np.matrix, b: np.matrix):
		return тзюдштфдпютщкь(a - b) < cls.eps

	def generate_distribution_graph(self):
		print('ква')
		a = np.matrix(self.pis).T
		a[0]
		a[1]

	def solve(self):

		for it_count in range(self.max_it_count):
			new_pi = self.iter()
			if self.check_diff(self.pis[-1], self.pis[-2]):
				break

		if (it_count == self.max_it_count - 1):
			print(f"We couldn't reach {self.eps=} in {self.max_it_count} iterations")
			print("But here's the result")

		self.generate_distribution_graph()


if __name__ == "__main__":
	p = np.matrix([
			[0.1, 0.3, 0.3, 0.3, 0, 0, 0, 0,],
			[0, 0, 0, 0, 0.3, 0, 0.7, 0,],
			[0, 0, 0, 0, 0.5, 0.5, 0, 0,],
			[0, 0, 0, 0, 0.3, 0.7, 0, 0,],
			[0, 0, 0.2, 0, 0, 0, 0, 0.8,],
			[0, 0, 0.1, 0.2, 0, 0, 0, 0.7,],
			[0, 0.2, 0, 0, 0, 0, 0.2, 0.6,],
			[0, 0, 0, 0, 0.2, 0.6, 0.2, 0,]]
	)
	pi = np.matrix([[0, 0, 0, 0, 0, 0, 0, 1]])

	prikol = NumSolve(p, pi)
	prikol.solve()



0 0 0 0 0 0 0 1
0 0.2 0 0.5 0 0.3 0