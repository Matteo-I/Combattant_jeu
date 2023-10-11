from collections import deque
from warnings import warn


class Queue:
    """An implementation of a Queue
    """

    def __init__(self):
        self._file = deque()

    def is_empty(self):
        """
        Return True if the queue is empty, False otherwise
        """
        return len(self._file) == 0

    def enqueue(self, element):
        """
        Add an element to the queue.
        Return the queue
        """
        self._file.appendleft(element)
        return repr(self)

    def dequeue(self):
        """
        pop the head element of the queue
        return the element
        If the queue is empty, raise IndexError exception.
        """
        return self._file.pop()

    def head(self):
        """
        return the head of the queue without removing it.
        If the queue is empty, raise IndexError exception.
        """
        value=self._file.pop()
        self._file.append(value)
        return value

    def size(self):
        """
        read the size of the queue
        return the size as an integer.
        """
        return len(self._file)

    def isEmpty(self):
        """
        (deprecated, use is_empty instead)
        """
        warn('This method is deprecated.', DeprecationWarning, stacklevel=2)
        return self.is_empty()
    
    def __repr(self):
        return str(self._file)