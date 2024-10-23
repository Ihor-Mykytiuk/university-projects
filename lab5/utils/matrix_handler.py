#matrix_handler.py
import numpy as np


class MatrixHandler:
    def __init__(self):
        self.matrix = None

    def generate_matrix(self, m, n):
        """Генерує матрицю розміру m x n з випадковими числами"""
        if m < 1 or n < 1:
            raise ValueError("Помилка: розміри матриці повинні бути більше 0")
        self.matrix = np.random.randint(1, 101, size=(m, n))
        return self.matrix

    def sum_columns(self, even=True):
        """Обчислює суму елементів парних або непарних стовпців"""
        if self.matrix is None:
            raise ValueError("Помилка: матриця не згенерована")

        if even:
            column_indices = range(0, self.matrix.shape[1], 2)
        else:
            column_indices = range(1, self.matrix.shape[1], 2)

        return np.sum(self.matrix[:, column_indices])

    def swap_min_max_in_rows(self):
        """Міняє місцями мінімальний і максимальний елементи в кожному рядку"""
        if self.matrix is None:
            raise ValueError("Помилка: матриця не згенерована")

        transformed_matrix = self.matrix.copy()
        for i, row in enumerate(transformed_matrix):
            min_index = np.argmin(row)
            max_index = np.argmax(row)
            transformed_matrix[i][min_index], transformed_matrix[i][max_index] = (
                transformed_matrix[i][max_index],
                transformed_matrix[i][min_index],
            )
        return transformed_matrix
