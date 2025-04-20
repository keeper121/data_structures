class HashNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

    def __str__(self):
        return f"({self.key}: {self.val})"


class HashMap:
    def __init__(self, capacity=10):
        """
        Initializes the hashmap with a fixed-size array of buckets (linked lists).
        """
        self.capacity = capacity
        self.buckets = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        """
        Computes hash index for the key.
        """
        return hash(key) % self.capacity

    def put(self, key, value):
        """
        Inserts or updates a key-value pair.
        If key exists, updates value. Otherwise, adds new node to bucket.
        Time: O(1) average, O(N) worst-case (linked list length).
        """
        index = self._hash(key)
        node = self.buckets[index]

        if not node:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return True

        while node:
            if node.key == key:
                node.val = value
                return True
            if not node.next:
                break
            node = node.next

        node.next = HashNode(key, value)
        self.size += 1
        return True

    def get(self, key):
        """
        Retrieves value by key.
        Returns None if not found.
        Time: O(1) average, O(N) worst-case.
        """
        index = self._hash(key)
        node = self.buckets[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return None

    def remove(self, key):
        """
        Removes key-value pair by key.
        Returns removed value or None.
        Time: O(1) average, O(N) worst-case.
        """
        index = self._hash(key)
        node = self.buckets[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return node.val
            prev = node
            node = node.next

        return None

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
        for bucket in self.buckets:
            node = bucket
            while node:
                yield (node.key, node.val)
                node = node.next


if __name__ == "__main__":
    hashmap = HashMap()

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

    print("OK!")