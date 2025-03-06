class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=new_node

    def printLinkedlist(self):
        current = self.head;
        while current:
            print(current.data,end="->")
            current=current.next
        print(None)

singly_linked_list = singlyLinkedList()
singly_linked_list.append(1)
singly_linked_list.append(2)
singly_linked_list.append(3)
singly_linked_list.printLinkedlist()