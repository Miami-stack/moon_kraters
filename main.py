import os
import warnings

import numpy as np


def get_value_from_file(filename: str) -> np.ndarray:
    """
    Читает файл и преобразовывает его в 2д массив

    """
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, filename)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        my_file = np.loadtxt(file_path).astype(int)
        return my_file


def calculate(matrix1: np.ndarray, query1: np.ndarray) -> str:
    """

    Эта функция находит и подсчитывает кратеры

    """
    searchlist = []
    t = all(matrix1[0, :] == 1)
    if t:
        searchlist.append(t)
    for row in matrix1:
        search = all(x in row for x in query1)
        if search is True:
            searchlist.append(search)

    return f"Количество краторов {len(searchlist)}"


matrix = get_value_from_file('test_file')
query = np.array([1, 0])

print(calculate(matrix, query))

