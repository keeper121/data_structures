class HashNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

    def __str__(self):
        return f"({self.key}: {self.val})"


class LinkedHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * self.capacity
        self.size = 0
        self.key_order = []  # maintains insertion order TODO implement double linked list

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        node = self.buckets[index]

        if not node:
            self.buckets[index] = HashNode(key, value)
            self.key_order.append(key)
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
        self.key_order.append(key)
        self.size += 1
        return True

    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def remove(self, key):
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
                if key in self.key_order:
                    self.key_order.remove(key)
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
        for key in self.key_order:
            yield (key, self.get(key))


if __name__ == "__main__":
    hashmap = LinkedHashMap()

    hashmap.put("apple", 1)
    hashmap.put("banana", 2)
    hashmap.put("banana2", 2)
    hashmap.put("banana4", 2)
    hashmap.put("banana3", 2)
    hashmap["orange"] = 3
    hashmap["banana"] = 10  # update

    assert hashmap.get("apple") == 1
    assert hashmap["banana"] == 10
    assert hashmap.remove("orange") == 3
    assert "banana" in hashmap
    del hashmap["banana"]
    assert "banana" not in hashmap

    print("Key order:")
    for key, value in hashmap:
        print(f"{key} => {value}")

    print("OK!")