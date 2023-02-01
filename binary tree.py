class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
        
    def print_tree(self):
        space = ' ' * self.get_level()
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def built_tree():
    root = TreeNode("Elec")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    cell = TreeNode("Cell")
    cell.add_child(TreeNode("iPhone"))
    root.add_child(laptop)
    root.add_child(cell)
    return root

if __name__=='__main__':
    root = built_tree()
    root.print_tree()
    pass
    