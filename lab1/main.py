from __future__ import annotations
import numpy as np
import math
# from lab1.simplex_method import *
# from lab1.tableau import *


class Simplex:
    """Simplex Method class"""
    a: np.array
    b: np.array
    c: np.array
    is_max: bool
    print_steps: bool
    tableau: np.array

    def __init__(self, a: np.array, b: np.array, c: np.array, is_max: bool, print_steps: bool = False):
        self.a = a
        self.b = b 
        self.c = c
        self.ans = 0
        self.is_max = is_max
        self.print_steps = print_steps
        self.to_tableau()

    def to_tableau(self):
        """
        Creates a tableau looking like
        AA...AAB
        ........
        AA...AAB
        CC...CC0
        """
        xb = np.column_stack((self.a, self.b.T))
        z = np.column_stack(([self.c], [[self.ans]]))
        self.tableau = np.vstack((xb, z))

    @classmethod
    def read_from_file(cls, path: str) -> cls:
        """Reads data written in file using specific format, return Simplex class"""
        with open(path, "r") as f:
            is_max = False
            if f.readline().strip() == 'max':
                is_max = True

            f.readline()
            c = [float(num) for num in f.readline().strip().split(',')]
            f.readline()

            a_matrix = []
            for line in f:
                if not line.strip():
                    break
                a_matrix.append([float(num) for num in line.strip().split(',')])

            b_matrix = [float(num) for num in f.readline().strip().split(',')]
            return cls(np.array(a_matrix), np.array(b_matrix), np.array(c), is_max)

    def can_be_improved(self) -> bool:
        """Returns true if ans could be improved <=> any c[j] > 0"""
        return any(x > 0 for x in self.c) if self.is_max else any(x < 0 for x in self.c)

    def find_solving_column(self) -> int:
        """Returns index of column that could be improved <=> j, c[j] >= c[i], i = 0..len(c)"""
        return np.argmax(self.c) if self.is_max else np.argmin(self.c)

    def find_solving_row(self, column_index: int) -> int:
        """Returns index of row with minimal restriction"""
        restrictions = []
        for row_index in range(self.a.shape[0]):
            el = self.a[row_index][column_index]
            restrictions.append(math.inf if el <= 0 else self.b[row_index] / el)

        row_index = restrictions.index(min(restrictions))

        if restrictions[row_index] == math.inf:
            raise Exception('No answer could be found. Range of valid values is infinite')
        return row_index

    def next_step(self):
        """Make iteration: find restrictions, edit tableau"""
        solving_column_index = self.find_solving_column()
        solving_row_index = self.find_solving_row(solving_column_index)

        self.b[solving_row_index] /= self.a[solving_row_index][solving_column_index]
        self.a[solving_row_index] /= self.a[solving_row_index][solving_column_index]

        for row_index in range(self.a.shape[0]):
            if row_index == solving_row_index:
                continue

            self.b[row_index] -= self.b[solving_row_index] * self.a[row_index][solving_column_index]
            self.a[row_index] -= self.a[solving_row_index] * self.a[row_index][solving_column_index]

        self.ans -= self.b[solving_row_index] * self.c[solving_column_index]
        self.c -= self.a[solving_row_index] * self.c[solving_column_index]

        self.to_tableau()

    def solve(self) -> float:
        """Solves linear equasion system using simplex method"""
        if self.print_steps:
            print(self.tableau)

        while self.can_be_improved():
            self.next_step()

            if self.print_steps:
                print(self.tableau)

        return -self.ans

    @classmethod
    def is_basic(cls, column: np.array) -> bool:
        return sum(column) == 1 and column.tolist().count(0) == len(column) - 1

    def get_solution(self):
        columns = self.tableau.T
        solutions = []
        for column in columns[:-1]:
            solution = 0
            if self.is_basic(column):
                one_index = column.tolist().index(1)
                solution = columns[-1][one_index]
            solutions.append(solution)
        
        return solutions


if __name__ == '__main__':
    # simplex = read_from_file('./input-files/first.txt')
    simplex = Simplex.read_from_file('./input-files/second.txt')
    print(simplex.solve())
    print(simplex.get_solution())
