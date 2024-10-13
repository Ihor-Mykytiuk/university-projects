class Node:
    def __init__(self, data):
        self.data = data  # Значення вузла
        self.next = None  # Посилання на наступний вузол


class QList:
    def __init__(self):
        self.head = None

    # Повертає перший елемент і видаляє його зі списку.
    def take_first(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    # Повертає останній елемент і видаляє його зі списку.
    def take_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next is not None:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    # Повертає елемент на зазначеній позиції і видаляє його зі списку.
    def take_at(self, index):
        if self.head is None:
            return None
        if index == 0:
            return self.take_first()
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                return None
            current = current.next
        if current.next is None:
            return None
        data = current.next.data
        current.next = current.next.next
        return data

    # Міняє місцями два елементи списку на зазначених позиціях.
    def swap(self, index1, index2):
        if index1 == index2:
            return
        if index1 > index2:
            index1, index2 = index2, index1
        current = self.head
        for i in range(index1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        node1 = current
        for i in range(index2 - index1 - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        node2 = current
        node1.data, node2.data = node2.data, node1.data

    # Виконує видалення останнього елемента списку.
    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    # Виконує видалення першого елемента списку.
    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
