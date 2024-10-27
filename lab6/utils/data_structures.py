class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None  # Початковий вузол списку

    def append(self, data):
        """Додає новий вузол в кінець списку"""
        new_node = SNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Додає новий вузол в початок списку"""
        new_node = SNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        """Виконує видалення першого елемента списку"""
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last(self):
        """Виконує видалення останнього елемента списку"""
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def take_first(self):
        """Повертає перший елемент і видаляє його зі списку"""
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def take_last(self):
        """Повертає останній елемент і видаляє його зі списку"""
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def take_at(self, index):
        """Повертає елемент на зазначеній позиції і видаляє його зі списку"""
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

    def swap(self, index1, index2):
        """Міняє місцями два елементи списку на зазначених позиціях"""
        if index1 == index2:
            return
        if index1 > index2:
            index1, index2 = index2, index1
        current = self.head
        for i in range(index1):
            if current.next is None:
                return
            current = current.next
        first_node = current
        for i in range(index2 - index1):
            if current.next is None:
                return
            current = current.next
        second_node = current
        first_node.data, second_node.data = second_node.data, first_node.data

    def insert(self, index, data):
        """Вставляє новий вузол на зазначену позицію"""
        if index == 0:
            self.prepend(data)
            return
        new_node = SNode(data)
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        """Повертає рядкове представлення списку"""
        def node_generator():
            current = self.head
            while current:
                yield str(current.data)
                current = current.next

        return " -> ".join(node_generator())
