class Stack:
    def __init__(self):
        self._buffer = []

    def push(self, val) -> None:
        """
        Put `val` in the buffer; O(1)
        """
        self._buffer.append(val)

    def pop(self):
        """
        Deletes the last element from the `buffer` and returns it; O(1)
        """
        return self._buffer.pop()

    def get(self):
        """
        Returns the last element the `buffer`; O(1)
        """
        return self._buffer[-1] if self._buffer else None

    def __len__(self):
        return len(self._buffer)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.pop() == 2
    assert s.get() == 1
    assert s.pop() == 1
    assert s.get() is None
    print("OK!")