import json
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root
    
    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root
    
    def insert(self, key):
        if self.root is None:
            self.root = AVLNode(key)
        else:
            self.root = self._insert(self.root, key)
            
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        self.update_height(node)
        balance = self.get_balance(node)
        
        if balance > 1:
            if key < node.left.key:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        if balance < -1:
            if key > node.right.key:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
        return node
    
    def delete(self, key):
        if self.root is None:
            return
        else:
            self.root = self._delete(self.root, key)
            
    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

        
    def print_tree(self, node):
        if node is None:
            return None
        return {
            "key": node.key,
            "left": self.print_tree(node.left),
            "right": self.print_tree(node.right),
            "height": node.height
        }
        
my_avl_tree = AVLTree()
# numbers = [1, 2, 3, 4, 5, 6, 23, 26, 21, 20, 11]
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for char in characters:
    my_avl_tree.insert(char)
# print(json.dumps(my_avl_tree.print_tree(my_avl_tree.root), indent=4))
# print("=======================================")

my_avl_tree.delete("E")
print(json.dumps(my_avl_tree.print_tree(my_avl_tree.root), indent=4))
print("=======================================")