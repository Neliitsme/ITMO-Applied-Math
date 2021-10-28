import numpy as np


def read_from_file(path: str) -> (bool, np.array, np.array, np.array):
    f = open(path, "r")

    is_max = False
    if f.readline().strip() == 'max':
        is_max = True

    f.readline()
    func = [float(num) for num in f.readline().strip().split(',')]
    f.readline()

    a_matrix = []
    for line in f:
        if not line.strip():
            break
        a_matrix.append([float(num) for num in line.strip().split(',')])

    b_matrix = [float(num) for num in f.readline().strip().split(',')]
    return is_max, np.array(func), np.array(a_matrix), np.array(b_matrix)


if __name__ == '__main__':
    is_max, f, a, b = read_from_file('./input-files/first.txt')
    print(a)
