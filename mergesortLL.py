class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = None

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.val, end='->')
            curr = curr.next
        print()
    
    def mergeSort(self):
        curr = self.head
        def merger(head1, head2):
            merged = Node(-1)
            temp = merged

            while head1 != None and head2 != None:
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next

            while head1 != None:
                temp.next = head1
                head1 = head1.next
                temp = temp.next
            while head2 != None:
                temp.next = head2
                head2 = head2.next
                temp = temp.next
            
            return merged.next
        
        if curr.next == None:
            return curr
        
        mid = self.findMid()
        head2 = mid.next
        mid.next = None
        newHead1 = curr.mergeSort()
        newHead2 = head2.mergeSort()
        finalHead = merger(newHead1, newHead2)
        return finalHead

    def findMid(self):
        currSlow = self.head
        currFast = currSlow.next

        while currFast != None and currFast != None:
            currSlow = currSlow.next
            currFast = currFast.next.next
        return currSlow


ll = LinkedList()
ll.head = Node(5)
node1 = Node(1)
node2 = Node(7)
node3 = Node(3)
node4 = Node(2)
node5 = Node(4)
node6 = Node(8)
ll.head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ll.print()
print(ll.mergeSort())