# array_handler.py
import numpy as np

class ArrayHandler:
    def __init__(self):
        self.array = []

    def create_random_array(self, size):
        """Створює масив випадкових чисел."""
        if size < 2:
            raise ValueError("Розмір масиву має бути більшим за 1.")
        self.array = np.random.randint(1, 101, size=size).tolist()
        return self.array

    def create_array_from_input(self, str_array):
        """Створює масив з введених користувачем значень."""
        self.array = list(map(int, str_array.split()))
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
