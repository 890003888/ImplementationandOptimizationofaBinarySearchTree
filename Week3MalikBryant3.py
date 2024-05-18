class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(self.root, key)

    def _add(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        elif node.val == key:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp_val = self.find_min_node(node.right).val
            node.val = temp_val
            node.right = self._delete(node.right, temp_val)
        return node

    def find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return 1 + max(left_height, right_height)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

# Usage
bt = BinaryTree()
values = [5, 3, 7, 1, 4, 6, 9]
for v in values:
    bt.add_node(v)

print("Search for 4:", bt.search(4))
print("Search for 10:", bt.search(10))
print("Minimum value:", bt.find_min())
print("Maximum value:", bt.find_max())
bt.delete(7)
print("Inorder traversal after deleting 7:", bt.inorder())
print("Height of the tree:", bt.height())

