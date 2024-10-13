class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        else:
            raise IndexError("Attempt to pop from an empty stack")

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            raise IndexError("Attempt to peek at an empty stack")


    class Queue:
        def __init__(self):
            self.__queue = []

        def enqueue(self, item):
            self.__queue.append(item)

        def dequeue(self):
            if not self.is_empty():
                return self.__queue.pop(0)  # Remove the first element
            else:
                raise IndexError("Attempt to dequeue from an empty queue")

        def is_empty(self):
            return len(self.__queue) == 0

        def head(self):
            if not self.is_empty():
                return self.__queue[0]  # Return the first element
            else:
                raise IndexError("Attempt to peek at an empty queue")

class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            raise IndexError("Attempt to dequeue from an empty queue")

    def is_empty(self):
        return len(self.__queue) == 0

    def head(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            raise IndexError("Attempt to get the head element of an empty queue")
