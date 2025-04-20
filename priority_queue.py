class MinHeap:
    def __init__(self):
        self._buffer = []

    def push(self, item):
        """Insert a tuple into the heap; O(log n)"""
        self._buffer.append(item)
        self._sift_up(len(self._buffer) - 1)

    def pop(self):
        """Remove and return the smallest tuple; O(log n)"""
        if not self._buffer:
            raise IndexError("pop from empty heap")

        self._swap(0, len(self._buffer) - 1)
        smallest = self._buffer.pop()
        self._sift_down(0)
        return smallest

    def _sift_up(self, idx):
        """Restore the heap property; O(log n)"""
        parent = (idx - 1) // 2
        if idx > 0 and self._buffer[idx] < self._buffer[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        """Restore the heap property; O(log n)"""
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self._buffer) and self._buffer[left] < self._buffer[smallest]:
            smallest = left
        if right < len(self._buffer) and self._buffer[right] < self._buffer[smallest]:
            smallest = right

        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self._buffer[i], self._buffer[j] = self._buffer[j], self._buffer[i]

    def __len__(self):
        return len(self._buffer)

    def __iter__(self):
        for val in self._buffer:
            yield val

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def push(self, val, priority=None):
        """Puts the value with the priority to the buffer; O(log n)"""
        if priority is not None and priority < 0:
            raise ValueError("Priority can't be bellow zero")

        if priority is None:
            # Use default priority for
            priority = -1

        self.heap.push((priority, val))

    def pop(self):
        """Returns the value with the lowest priority from the buffer; O(log n)"""

        _, val = self.heap.pop()
        return val

    def __iter__(self):
        for priority, val in self.heap:
            yield val

    def __len__(self):
        return len(self.heap)

if __name__ == "__main__":
    priority_queue = PriorityQueue()

    priority_queue.push(val=1, priority=10)
    priority_queue.push(val=2, priority=5)
    priority_queue.push(val=3, priority=8)
    assert priority_queue.pop() == 2
    assert len(priority_queue) == 2
    assert list(priority_queue) == [3, 1]

    print("OK!")
