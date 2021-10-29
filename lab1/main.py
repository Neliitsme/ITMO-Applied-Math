import numpy as np
from lab1.simplex_method import *
from lab1.tableau import *


def read_from_file(path: str) -> (bool, np.array, np.array, np.array):
    f = open(path, "r")

    _is_max = False
    if f.readline().strip() == 'max':
        _is_max = True

    f.readline()
    _c = [float(num) for num in f.readline().strip().split(',')]
    f.readline()

    a_matrix = []
    for line in f:
        if not line.strip():
            break
        a_matrix.append([float(num) for num in line.strip().split(',')])

    b_matrix = [float(num) for num in f.readline().strip().split(',')]
    return _is_max, np.array(_c), np.array(a_matrix), np.array(b_matrix)


if __name__ == '__main__':
    # is_max, c, a, b = read_from_file('./input-files/first.txt')
    is_max = True
    c = np.array([1, 1, 0, 0, 0])
    a = np.array([[-1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1]])
    b = np.array([2, 4, 4])
    tableau = to_tableau(c, a, b)
    print(handle_table(tableau, [], []))
    # print(b)
