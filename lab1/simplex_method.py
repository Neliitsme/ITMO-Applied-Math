import sys

import numpy as np

t = np.array([[9, 9, 9], [1, -1, 3], [1, -2, 4], [3, -2, 1]])


def is_tale_ready_to_go(table: np.array) -> bool:
    for elem in table[-1][1:]:
        print(elem)
        if elem < 0:
            return True
    return False


def find_solving_column(table: np.array) -> int:
    return np.argmin(table[-1][1:]) + 1


def find_solving_row(table: np.array, solving_column_index: int) -> int:
    column = [e[solving_column_index] for e in table[:-1]]
    first_column = [e[0] for e in table[:-1]]
    if min(column) > 0:
        raise Exception('Конкретного численного ответа не существует. Область допустимых решений не ограничена.')
    min_ind = -1
    rel = sys.maxsize
    for i in range(len(column)):
        if abs(first_column[i]/column[i]) < rel and column[i] < 0:
            rel = abs(first_column[i]/column[i])
            min_ind = i
    return min_ind


def change_row_sign(table: np.array, solving_column_index: int, solving_row_index: int) -> np.array:
    for i in range(len(table.shape[1])):
        if i != solving_column_index:
            table[solving_row_index][i] *= -1
    return table


def calculate_rectangle_method(table: np.array, solving_column_index: int, solving_row_index: int) -> np.array:
    new_table = table.copy()
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


def handle_table(table: np.array, solving_x: list, free_x: list) -> float:
    while is_tale_ready_to_go(table):
        solving_column_index = find_solving_column(table)
        if table[-1][solving_column_index] >= 0:
            return table[-1][0]
        # if table[-1][solving_column_index] >= 0:
        #     raise Exception('aaa')
        solving_row_index = find_solving_row(table, solving_column_index)
        table_copy = table.copy()
        table_copy = calculate_rectangle_method(table_copy, solving_column_index, solving_row_index)
        table_copy = change_row_sign(table_copy, solving_column_index, solving_row_index)
        table_copy = divide_to_solving_element(table_copy, solving_column_index, solving_row_index)
        table = table_copy


# print(t.shape[1])
# print(find_solving_column(t))
# print(find_solving_row(t, 1))


