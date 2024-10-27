class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Attempt to pop from an empty stack")
        return self.__stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Attempt to get top element from an empty stack")
        return self.__stack[-1]

    def is_empty(self):
        return not bool(self.__stack)

    def swap(self, other_stack):
        """Swaps stack other with this stack"""
        self.__stack, other_stack.__stack = other_stack.__stack, self.__stack

    def __str__(self):
        return "top\n " + "\n".join(map(str, self.__stack[::-1])) + "\n bottom"


class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Attempt to dequeue from an empty queue")
        return self.__queue.pop(0)

    def head(self):
        if self.is_empty():
            raise IndexError("Attempt to get head element from an empty queue")
        return self.__queue[0]

    def is_empty(self):
        return not bool(self.__queue)

    def swap(self, other_queue):
        """Swaps queue other with this queue"""
        self.__queue, other_queue.__queue = other_queue.__queue, self.__queue
    def size(self):
        return len(self.__queue)
    def __str__(self):
        return "head\n" + "\n".join(map(str, self.__queue)) + "\n tail"
