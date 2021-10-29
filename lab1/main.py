import numpy as np
from lab1.simplex_method import *
from lab1.tableau import *


class Simplex:
    """Simplex Method class"""
    a: np.array
    b: np.array
    c: np.array
    is_max: bool
    tableau: np.array

    def __init__(self, a: np.array, b: np.array, c: np.array, is_max: bool):
        self.a = a
        self.b = b 
        self.c = c
        self.ans = 0
        self.is_max = is_max
        self.to_tableau()

    def to_tableau(self):
        """
        Creates a tableau looking like
        AA...AAB
        ........
        AA...AAB
        CC...CC0
        """
        xb = [eq + [x] for eq, x in zip(self.a, self.b)]
        z = self.c + [self.ans]
        self.tableau = np.array(xb + [z])

    @classmethod
    def read_from_file(cls, path: str) -> Simplex:
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
        return any(x > 0 for x in self.c)

    def find_solving_column(self) -> int:
        """Returns index of column that could be improved <=> j, c[j] >= c[i], i = 0..len(c)"""
        return np.argmax(self.c)

    def find_solving_row(self, column_index: int) -> int:
        """Returns index of row with minimal restriction"""
        restrictions = []
        for row_index in range(self.a):
            el = self.a[row_index][column_index]
            restrictions.append(math.inf if el <= 0 else self.b[row_index] / el)

        row_index = restrictions.index(min(restrictions))

        if restrictions[row_index] == math.inf:
            raise Exception('No answer could be found. Range of valid values is infinite')
        return row_index

    def change_row_sign(table: np.array, solving_column_index: int, solving_row_index: int) -> np.array:
        for i in range(len(table.shape[1])):
            if i != solving_column_index:
                table[solving_row_index][i] *= -1
        return table

    def calculate_rectangle_method(self, solving_column_index: int, solving_row_index: int) -> np.array:
        new_table = self.tableau.copy()
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                if not (i == solving_column_index or j == solving_row_index):
                    new_table[i, j] = table[i, j] * table[solving_row_index, solving_column_index] - table[i, solving_column_index] * table[solving_row_index, j]
        return new_table

    def divide_to_solving_element(table: np.array, solving_column_index: int, solving_row_index: int) -> np.array:
        solving_element = table[solving_row_index, solving_column_index]
        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                table[i][j] /= solving_element
        return table

    def solve(self, solving_x: list, free_x: list) -> float:
        """Solves linear equasion system using simplex method"""
        while self.can_be_improved():
            solving_column_index = self.find_solving_column()
            solving_row_index = self.find_solving_row(solving_column_index)
            
            table_copy = table.copy()
            table_copy = calculate_rectangle_method(table_copy, solving_column_index, solving_row_index)
            table_copy = change_row_sign(table_copy, solving_column_index, solving_row_index)
            table_copy = divide_to_solving_element(table_copy, solving_column_index, solving_row_index)
            table = table_copy

        return self.ans



if __name__ == '__main__':
    # aboba = read_from_file('./input-files/first.txt')
    simplex = Simplex.read_from_file('./input-files/second.txt')
    print(solve(simplex.tableau, [], []))
    # print(b)
