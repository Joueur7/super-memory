class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def in_order_traversal(self):
        elements = []
        #left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #root node
        elements.append(self.data)

        #right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        
    
def build_tree(elements):
        root = BinarySearchTree(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])
        
        return root

if __name__ == '__main__':
    numbers = [17,98,12,34,87,96,68,2,4,1,6]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(12))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())



