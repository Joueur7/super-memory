class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return

        llist=''
        itr = self.head
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
            
        print(llist)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(5)
    ll.insert_at_begin(89)
    ll.print()

