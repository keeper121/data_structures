class ArrayList:
    def __init__(self):
        self._capacity = 4
        self._size = 0
        self._data = [None] * self._capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self._size:
            self._data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty list")
        value = self._data[self._size - 1]
        self._size -= 1
        return value

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]


if __name__ == "__main__":
    array_list = ArrayList()
    array_list.append(1)
    array_list.append(2)
    array_list.append(3)
    assert array_list.pop() == 3
    assert len(array_list) == 2
    assert list(array_list) == [1, 2]

    print("OK!")