class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Attempt to pop from an empty stack")
        return self.__items.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Attempt to get top element from an empty stack")
        return self.__items[-1]

    def is_empty(self):
        return not bool(self.__items)

    def swap(self, other_stack):
        self.__items, other_stack.__items = other_stack.__items, self.__items

    def __str__(self):
        return "top\n" + "\n".join(map(str, self.__items[::-1])) + "\nbottom"


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Attempt to dequeue from an empty queue")
        return self.__items.pop(0)

    def head(self):
        if self.is_empty():
            raise IndexError("Attempt to get head element from an empty queue")
        return self.__items[0]

    def is_empty(self):
        return not bool(self.__items)

    def swap(self, other_queue):
        self.__items, other_queue.__items = other_queue.__items, self.__items

    def size(self):
        return len(self.__items)

    def __str__(self):
        return "head\n" + "\n".join(map(str, self.__items)) + "\ntail"
