"""Скрипт подсчета лунных кратеров."""

import os
import sys
from typing import Any
import numpy as np


def get_value_from_file(file: str) -> object:
    """Читает файл и преобразовывает его в 2д массив."""

    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, file)
    if os.stat(file_path).st_size == 0:
        print("Файл пустой")
        sys.exit(0)
    my_file = np.loadtxt(file_path).astype(int).tolist()
    return my_file


def calculate(matrix1: Any, query1: list) -> int:
    """Эта функция находит и подсчитывает кратеры."""
    searchlist = []
    if all(matrix1[matrix1[0][:] == 1]):
        searchlist.append(1)
    for row in matrix1:
        search = all(x in row for x in query1)
        if search is True:
            searchlist.append(search)

    return len(searchlist)


matrix = get_value_from_file('test_file')
query = [1, 0]

print(f"Количество кратеров: {calculate(matrix, query)}")
