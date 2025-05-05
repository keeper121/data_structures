import threading
from hashmap import HashMap

class ConcurrentHashMap(HashMap):
    def __init__(self, capacity=10):
        """
        Initializes the hashmap with a fixed-size array of buckets (linked lists).

        Use lock for each bucket
        """

        super().__init__(capacity=capacity)
        self.locks = [threading.RLock() for _ in range(self.capacity)]

    def put(self, key, value):
        """
        Inserts or updates a key-value pair.
        If key exists, updates value. Otherwise, adds new node to bucket.
        Time: O(1) average, O(N) worst-case (linked list length).
        """
        index = self._hash(key)
        with self.locks[index]:
            return super().put(key, value)

    def get(self, key):
        """
        Retrieves value by key.
        Returns None if not found.
        Time: O(1) average, O(N) worst-case.
        """
        index = self._hash(key)
        with self.locks[index]:
            return super().get(key)

    def remove(self, key):
        """
        Removes key-value pair by key.
        Returns removed value or None.
        Time: O(1) average, O(N) worst-case.
        """
        index = self._hash(key)
        with self.locks[index]:
            return super().remove(key)

    def increment(self, key, delta=1):
        index = self._hash(key)
        with self.locks[index]:
            val = super().get(key) or 0
            super().put(key, val + delta)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.get(key) is not None

    def __len__(self):
        return self.size

    def __iter__(self):
        for i, bucket in enumerate(self.buckets):
            with self.locks[i]:
                node = bucket
                while node:
                    yield (node.key, node.val)
                    node = node.next

def test_put_fn(hashmap, key):
    n = 100
    for _ in range(n):
        hashmap.increment(key)

if __name__ == "__main__":
    hashmap = ConcurrentHashMap()

    hashmap.put("apple", 1)
    hashmap.put("banana", 2)
    hashmap["orange"] = 3
    hashmap["banana"] = 10  # update

    assert hashmap.get("apple") == 1
    assert hashmap["banana"] == 10
    assert hashmap.remove("orange") == 3
    assert hashmap.remove("notfound") is None
    assert "banana" in hashmap
    del hashmap["banana"]
    assert "banana" not in hashmap

    for key, value in hashmap:
        print(f"{key} => {value}")

    hashmap["apple"] = 0
    thread1 = threading.Thread(target=test_put_fn, args=(hashmap, "apple"))
    thread2 = threading.Thread(target=test_put_fn, args=(hashmap, "apple"))
    thread3 = threading.Thread(target=test_put_fn, args=(hashmap, "apple"))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print(hashmap["apple"])
    assert hashmap["apple"] == 100 * 3

    print("OK!")