class Node:
    def __init__(self, val, next = 0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = None

    def __insert_at_beg__(self, new):
        NewNode = Node(new)
        NewNode.next = self.head
        self.head = NewNode
    def __insert_at_end__(self, new):
        NewNode = Node(new)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = NewNode
    def __insert_at__idx__(self, new, idx):
        newNode = Node(new)
        i = 0

        curr = self.head
        while i < idx-1:
            curr = curr.next
            i += 1
        temp = curr.next
        curr.next = newNode
        newNode.next = temp


    def print(self):
        curr = self.head
        while curr is not None:
            print(str(curr.val) + " -> ", end="")
            curr = curr.next
            if curr == self.head:
                break
        print(end="\n")
    
    def insert(self, new, id):
        if id == 'start':
            self.__insert_at_beg__(new)
        elif id == 'end':
            self.__insert_at_end__(new)
        else:
            self.__insert_at__idx__(new, int(id))
    
    def remove(self, to_rem):
        curr = self.head
        if curr is not None:
            if curr.val == to_rem:
                self.head = curr.next
                curr = None
                return

        while curr is not None:
            if curr.val == to_rem:
                break
            prev = curr
            curr = curr.next

        if curr == None:
            return
        
        prev.next = curr.next
        curr = None
    
    def remove_in_O1(self, val_node):
        curr = self.head
        while curr.val != val_node:
            curr = curr.next
        
        prev = curr
        curr = curr.next
        prev.val = curr.val
        next = curr.next
        prev.next = next
        curr = None

    
    def sum(self):
        curr = self.head
        ans = 0
        while curr != None:
            ans = ans + curr.val
            curr = curr.next
        return ans
    
    def reverse(self, list_name):
        prev = None
        curr = list_name.head

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev
        return list_name
    
    def merge(self, list2):
        curr1 = self.head
        curr2 = list2.head
        while 1:
            curr1_next = curr1.next
            curr2_next = curr2.next

            curr1.next = curr2
            curr1 = curr1_next
            curr2.next = curr1
            curr2 = curr2_next

            if curr1.next == None:
                curr1.next = curr2
                break

            if curr2.next == None:
                curr2.next = curr1
                break
        list2.head = None

    def delete_duplicates(self):
        curr = self.head
        map = {}
        prev = None
        while curr != None:
            if curr.val not in map:
                map[curr.val] = 1
                prev = curr
                curr = curr.next
            else:
                next = curr.next
                prev.next = next
                curr = None
                curr = next
    def conv_to_circular(self):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = self.head
    
    def sort_bubble(self):
        curr = self.head
        while curr != None:
            nexxt = curr.next
            while nexxt != None:
                if nexxt.val < curr.val:
                    temp = curr.val
                    curr.val = nexxt.val
                    nexxt.val = temp
                nexxt = nexxt.next
            curr = curr.next
    
    
    def intersection(self, list2):
        curr = self.head

        while curr != None:
            curr2 = list2.head
            while curr2 != None:
                if curr2 == curr:
                    return curr.val
                curr2 = curr2.next
            curr = curr.next
    
    def reverse_in_groups(self, grp):
        curr = self.head
        return -1
    
    def palindrome(self):
        curr = self.head
        helper = LinkedList()
        helper = self.reverse(self)
        helper.print()
        curr2 = helper.head

        while curr != None:
            if curr.val != curr2.val:
                print("Not a Palindrome!")
                return -1
            curr = curr.next
            curr2 = curr2.next
        
        print("Palindrome!")
        return 1



list1 = LinkedList()
list1.head = Node(1)
list1.insert(2, 'end')
list1.insert(3, 'end')
list1.insert(4, 'end')
list1.insert(5, 'end')
list1.print()

list1.palindrome()








