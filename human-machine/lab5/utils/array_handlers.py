import numpy as np


class ArrayHandler:
    def __init__(self):
        self.array = []

    def create_random_array(self, size):
        """Створює масив випадкових чисел."""
        try:
            size = int(size)
        except ValueError:
            raise ValueError("Розмір масиву має бути цілим числом.")
        if size < 2:
            raise ValueError("Розмір масиву має бути більшим за 1.")
        self.array = np.random.randint(1, 101, size=size).tolist()
        return self.array

    def create_array_from_input(self, str_array):
        """Створює масив з введених користувачем значень."""
        try:
            self.array = list(map(int, str_array.split()))
        except ValueError:
            raise ValueError("Введіть числа через пробіл.")
        if len(self.array) < 2:
            raise ValueError("Масив має містити принаймні два елементи.")
        return self.array

    def transform(self):
        """Метод для трансформації масиву."""
        raise NotImplementedError("Цей метод має бути реалізований в підкласах.")

class TransformArray(ArrayHandler):
    def transform(self):
        """Перетворення масиву: додаємо перший елемент до парних, крім першого й останнього."""
        if not self.array:
            raise ValueError("Спочатку створіть масив.")
        first_element = self.array[0]
        transformed_array = [first_element]
        for i in range(1, len(self.array) - 1):
            if self.array[i] % 2 == 0:
                transformed_array.append(self.array[i] + first_element)
            else:
                transformed_array.append(self.array[i])
        transformed_array.append(self.array[-1])
        return transformed_array

class SortArray(ArrayHandler):
    def transform(self):
        """Перетворення масиву: спочатку парні, потім непарні елементи."""
        if not self.array:
            raise ValueError("Спочатку створіть масив.")
        even_elements = [x for x in self.array if x % 2 == 0]
        odd_elements = [x for x in self.array if x % 2 != 0]
        return even_elements + odd_elements


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
