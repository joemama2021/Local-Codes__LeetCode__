class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, val):
        node = ListNode(val, self.head)
        self.head = node
    
    def insert_at_end(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = ListNode(val)
    
    def insert_values(self, val_list):
        self.head = None
        for val
    
    def print(self):
        if self.head is None:
            print("Empty list")
            return
        
        itr = self.head
        strr = ''
        while itr:
            strr = strr + str(itr.val)+"->"
            itr = itr.next 
        
        print(strr)

ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(4)
ll.insert_at_beginning(3)
ll.insert_at_end(2)
ll.insert_at_beginning(1)
ll.print()