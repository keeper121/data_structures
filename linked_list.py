class LinkedNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = LinkedNode()
        self.tail = self.head
        self.n = 0

    def get(self, index = None):
        """
        Gets `val` from the linked list. If `index` is None, gets with O(1).
        If `index` is provided, finds the point with O(N).
        """
        if not self.n or index >= self.n:
            return None

        if index == 0:
            return self.head.next.val

        if index == self.n - 1:
            return self.tail.val

        i = 0
        node = self.head.next
        while node is not None and i != index:
            node = node.next
            i += 1

        return node.val

    def put(self, val, index = None) -> bool:
        """
        Inserts `val` into the linked list. If `index` is None, inserts with O(1).
        If `index` is provided, finds the insertion point with O(N).
        """
        if index is None:
            self.tail.next = LinkedNode(val)
            self.tail = self.tail.next
            self.n += 1
            return True

        if index >= self.n:
            return False

        i = 0
        node = self.head
        while node is not None and i != index:
            node = node.next
            i += 1

        if i == index:
            node.next = LinkedNode(val=val, next=node.next)
            self.n += 1
            return True

        return False

    def pop(self, index = None):
        """
        Pops `val` from the linked list with O(N).
        """
        if index is None:
            index = self.n - 1

        if not self.n or index >= self.n:
            return None

        i = 0
        node = self.head
        while node is not None and i != index:
            node = node.next
            i += 1

        val = node.next.val
        node.next = node.next.next
        self.n -= 1
        return val

    def __iter__(self):
        node = self.head.next
        while node is not None:
            yield node.val
            node = node.next

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.n

if __name__ == "__main__":
    linked_list = LinkedList()

    for i in range(5):
        linked_list.put(i)

    assert linked_list.get(4) == 4
    assert linked_list[0] == 0
    linked_list.put(val=100, index=2)
    assert linked_list[2] == 100
    assert linked_list.pop() == 4
    assert linked_list.pop() == 3
    assert linked_list.pop(1) == 1

    for l in linked_list:
        print(l, end=",")
    print()
    assert list(linked_list) == [0, 100, 2]

    print("OK!")