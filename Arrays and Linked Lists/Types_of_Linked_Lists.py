# 1- Singly linked list 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

linked_list = Linked_List()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next
        