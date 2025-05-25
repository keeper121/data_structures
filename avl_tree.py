import collections

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
        self.h = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def min_left_node(self, node):
        cur_node = node
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    @classmethod
    def get_balance(cls, node):
        if node is None:
            return 0

        return cls.get_height(node.left) - cls.get_height(node.right)

    @classmethod
    def get_height(cls, node):
        if node is None:
            return 0
        return node.h

    @classmethod
    def left_rotate(cls, node):
        if node is None:
            return None

        a = node
        b = node.right
        a.right = b.left
        b.left = a
        a.h = 1 + max(cls.get_height(a.left), cls.get_height(a.right))
        b.h = 1 + max(cls.get_height(b.left), cls.get_height(b.right))
        return b

    @classmethod
    def right_rotate(cls, node):
        if node is None:
            return None

        a = node
        b = node.left
        a.left = b.right
        b.right = a
        a.h = 1 + max(cls.get_height(a.left), cls.get_height(a.right))
        b.h = 1 + max(cls.get_height(b.left), cls.get_height(b.right))
        return b

    @classmethod
    def _rebalance_node(cls, node, val):
        # O(1)
        node.h = 1 + max(cls.get_height(node.left), cls.get_height(node.right))

        # right-right case -> left rotate
        balance = cls.get_balance(node)
        if balance < -1 and val > node.right.val:
            return cls.left_rotate(node)

        # left-left case -> right rotate
        if balance > 1 and val < node.left.val:
            return cls.right_rotate(node)

        # right-left case -> left-right rotate
        if balance < -1 and val < node.right.val:
            node.right = cls.right_rotate(node.right)
            return cls.left_rotate(node)

        # left-right case -> right-left rotate
        if balance > 1 and val > node.left.val:
            node.left = cls.left_rotate(node.left)
            return cls.right_rotate(node)
        return node

    def insert(self, val):
        # O(logN)
        def _insert_dfs(node, val):
            if node is None:
                return Node(val)

            if val < node.val:
                node.left = _insert_dfs(node.left, val)
            elif val > node.val:
                node.right = _insert_dfs(node.right, val)
            else:
                return node

            return self._rebalance_node(node, val)

        self.root = _insert_dfs(self.root, val)
        return True

    def get(self):
        # O(1)
        if self.root:
            return self.root.val

        return None

    def remove(self, val):
        # O(log N)
        def remove_dfs(node, val):
            if node is None:
                return None

            if val < node.val:
                node.left = remove_dfs(node.left, val)
            elif val > node.val:
                node.right = remove_dfs(node.right, val)
            else:
                # found node to delete
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = self.min_left_node(node.right)
                    node.val = min_node.val
                    node.right = remove_dfs(node.right, min_node.val)

            return self._rebalance_node(node, val)

        self.root = remove_dfs(self.root, val)

    def is_balanced(self, node=None):
        # O(log N)
        if node is None:
            node = self.root

        def check(node):
            if not node:
                return 0, True

            lh, left_bal = check(node.left)
            rh, right_bal = check(node.right)

            balanced = left_bal and right_bal and abs(lh - rh) <= 1
            return 1 + max(lh, rh), balanced

        _, balanced = check(node)
        return balanced

    def __repr__(self):
        # O(N)
        queue = collections.deque([self.root])

        levels = []
        while queue:
            level = []
            next_queue = []

            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    level.append("-")
                    next_queue.extend([None, None])
                else:
                    level.append(str(node.val))
                    next_queue.append(node.left)
                    next_queue.append(node.right)

            levels.append(level)
            if all(n is None for n in next_queue):
                break
            queue.extend(next_queue)

        lines = []
        max_level = len(levels)
        for i, level in enumerate(levels):
            space = " " * (2 ** (max_level - i - 1))
            between = " " * (2 ** (max_level - i) - 1)
            lines.append(space + between.join(level) + space)

        return "\n".join(lines) + "\n"

    def _depth(self, node):
        if not node:
            return 0
        return 1 + max(self._depth(node.left), self._depth(node.right))

if __name__ == "__main__":
    avl_tree = AVLTree()

    avl_tree.insert(1)
    avl_tree.insert(5)
    print(avl_tree)
    avl_tree.insert(3)
    avl_tree.insert(4)
    print(avl_tree)
    avl_tree.insert(2)
    avl_tree.insert(9)
    avl_tree.insert(8)
    print(avl_tree)

    avl_tree.remove(8)
    print(avl_tree)
    avl_tree.remove(3)
    print(avl_tree)
    avl_tree.remove(4)
    print(avl_tree)
    avl_tree.remove(9)
    print(avl_tree)
    print(f"{avl_tree.is_balanced()=}")

    print(avl_tree.root.val)
    print(avl_tree.get_height(avl_tree.root.left), avl_tree.get_height(avl_tree.root.right))

