class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key, value):
        def add_node(node, key, value):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            add_node(self.root, key, value)

    def remove(self, key):
        parent = None
        p = self.root
        is_leftChild = True

        while True:
            if p is None:
                return False
            if p.key == key:
                break
            elif key < p.key:
                parent = p
                is_leftChild = True
                p = p.left
            else:
                parent = p
                is_leftChild = False
                p = p.right

        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_leftChild:
                parent.left = p.right
            else:
                parent.right = p.right

        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_leftChild:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_leftChild = True

            while left.right is not None:
                parent = left
                left = left.right
                is_leftChild = False

            p.key = left.key
            p.value = left.value
            if is_leftChild:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self):
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self):
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self):
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
