class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = node(root)
    
    def _insert(self, val, pos):
        if val < pos.val:
            if pos.left is None:
                pos.left = node(val)
            else:
                self._insert(val, pos.left)
        elif val > pos.val:
            if pos.right is None:
                pos.right = node(val)
            else:
                self._insert(val, pos.right)
    
    def insert(self, val):
        if self.root is None:
            self.root = node(val)
        else:
            self._insert(val, self.root)
            
    
    def printTree(self, trlist1_type = None):
        if trlist1_type == "preorder":
            return self.preorder(self.root, "")

    def preorder(self, start, trlist1):
        if start:
            trlist1 += (str(start.val) + " - ")
            trlist1 = self.preorder(start.left, trlist1)
            trlist1 = self.preorder(start.right, trlist1)
        return trlist1

bt = BinaryTree(5)
bt.insert(1)
bt.insert(9)
bt.insert(4)
bt.insert(6)
bt.insert(3)
bt.insert(8)
bt.insert(2)

bt.printTree("preorder")


    