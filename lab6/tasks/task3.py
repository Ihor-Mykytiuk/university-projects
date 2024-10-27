import sys, random
from PySide6.QtWidgets import QApplication, QWidget
from lab6.ui.task3_interface import Ui_Form

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None  # Початковий вузол списку
        self.tail = None  # Кінцевий вузол списку

    def append(self, data):
        """Додає новий вузол в кінець списку"""
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Додає новий вузол в початок списку"""
        new_node = DNode(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove_first(self):
        """Виконує видалення першого елемента списку"""
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def remove_last(self):
        """Виконує видалення останнього елемента списку"""
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def take_first(self):
        """Повертає перший елемент і видаляє його зі списку"""
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def take_last(self):
        """Повертає останній елемент і видаляє його зі списку"""
        if self.head is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def take_at(self, index):
        """Повертає елемент на зазначеній позиції і видаляє його зі списку"""
        if self.head is None:
            return None
        if index == 0:
            return self.take_first()
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        if current is None:
            return None
        data = current.data
        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev
        return data

    def swap(self, index1, index2):
        """Міняє місцями два елементи списку на зазначених позиціях"""
        if index1 == index2:
            return

        if index1 > index2:
            index1, index2 = index2, index1

        prev1 = None
        current1 = self.head
        for i in range(index1):
            if current1 is None:
                return
            prev1 = current1
            current1 = current1.next

        prev2 = None
        current2 = self.head
        for i in range(index2):
            if current2 is None:
                return
            prev2 = current2
            current2 = current2.next

        if current1 is None or current2 is None:
            return

        if prev1 is not None:
            prev1.next = current2
        else:
            self.head = current2

        if prev2 is not None:
            prev2.next = current1
        else:
            self.head = current1

        current1.prev, current1.next, current2.prev, current2.next = current2.prev, current2.next, current1.prev, current1.next

        if current1.next is not None:
            current1.next.prev = current1
        else:
            self.tail = current1
        if current2.next is not None:
            current2.next.prev = current2
        else:
            self.tail = current2

    def insert(self, index, data):
        """Вставляє новий вузол на зазначену позицію"""
        if index == 0:
            self.prepend(data)
            return
        new_node = DNode(data)
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                return
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def clear(self):
        """Очищує список"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Повертає рядкове представлення списку"""
        def node_generator():
            current = self.head
            while current:
                yield str(current.data)
                current = current.next

        return " <-> ".join(node_generator())

class ExtendedDLinkedList(DLinkedList):
    def __init__(self):
        super().__init__()

    def swap_nodes(self, node1, node2):
        """Міняє місцями два вузли списку"""
        if node1 is None or node2 is None:
            return
        if node1.prev is not None:
            node1.prev.next = node2
        else:
            self.head = node2
        if node2.prev is not None:
            node2.prev.next = node1
        else:
            self.head = node1
        node1.prev, node1.next, node2.prev, node2.next = node2.prev, node2.next, node1.prev, node1.next
        if node1.next is not None:
            node1.next.prev = node1
        else:
            self.tail = node1
        if node2.next is not None:
            node2.next.prev = node2
        else:
            self.tail = node2

    def count(self, first, last, value):
        """Підраховує кількість входжень значення value в діапазоні позицій від first до last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        count = 0
        for i in range(last + 1):
            if i >= first and current.data == value:
                count += 1
            current = current.next
            if current is None:
                break
        return count

    def reverse(self, first, last):
        """Реверсує підсписок від позиції first до last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        for i in range(first):
            if current is None:
                raise ValueError("Позиція first виходить за межі списку.")
            current = current.next
        if current is None:
            raise ValueError("Позиція first виходить за межі списку.")
        first_node = current
        for i in range(last - first):
            if current is None:
                raise ValueError("Позиція last виходить за межі списку.")
            current = current.next
        if current is None:
            raise ValueError("Позиція last виходить за межі списку.")

        last_node = current
        while first_node != last_node and first_node.prev != last_node:
            self.swap_nodes(first_node, last_node)
            first_node = first_node.next
            last_node = last_node.prev

    def iter_swap(self, first, last):
        """Міняє місцями значення елементів списку в позиціях first та last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        for i in range(last + 1):
            if i == first:
                first_node = current
            if i == last:
                last_node = current
            current = current.next
            if current is None:
                break
        if current is None:
            raise ValueError("Позиція last виходить за межі списку.")
        first_node.data, last_node.data = last_node.data, first_node.data


