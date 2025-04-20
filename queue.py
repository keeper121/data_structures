import linked_list

class Queue:
    def __init__(self):
        self._buffer = linked_list.LinkedList()

    def put(self, val) -> bool:
        """
        Puts in the queue; O(1)
        """
        self._buffer.put(val)

        return False

    def get(self):
        """
        Gets from the queue; O(1)
        """
        return self._buffer.pop(index=0)

    def __iter__(self):
        yield self._buffer

    def __len__(self):
        return len(self._buffer)

if __name__ == "__main__":
    queue = Queue()

    queue.put(1)
    queue.put(2)
    queue.put(3)

    assert queue.get() == 1
    assert queue.get() == 2
    assert len(queue) == 1
    assert queue.get() == 3

    print("OK!")