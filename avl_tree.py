import collections

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
        self.h = 0

class AVLTree:
    # TODO balancing of the tree
    def __init__(self):
        self.root = None

    def min_left_node(self, node):
        cur_node = node
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        def add_dfs(node, val):
            if node is None:
                return Node(val)

            if val < node.val:
                node.left = add_dfs(node.left, val)
            elif val > node.val:
                node.right = add_dfs(node.right, val)
            else:
                # ?
                pass
            return node

        self.root = add_dfs(self.root, val)
        return True

    def get(self):
        if self.root:
            return self.root.val

        return None

    def remove(self, val):
        def remove_dfs(node, val):
            if node is None:
                return

            if val < node.val:
                node.left = remove_dfs(node.left, val)
            elif val > node.val:
                node.right = remove_dfs(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = self.min_left_node(node.right)
                    node.val = min_node.val
                    node.right = remove_dfs(node.right, min_node.val)
            return node

        return remove_dfs(self.root, val)

    def pop(self):
        pass

    def __repr__(self):
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
    avl_tree.insert(3)
    avl_tree.insert(4)
    avl_tree.insert(2)
    avl_tree.insert(0)
    avl_tree.insert(9)
    avl_tree.insert(8)
    print(avl_tree)

    avl_tree.remove(8)
    print(avl_tree)

    avl_tree.remove(3)
    print(avl_tree)

