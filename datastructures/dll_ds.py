class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLinkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        if not self.head:
            self.head= new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=new_node
        new_node.prev=last

    def printlist(self):
        current=self.head
        while current:
            print(current.data,end="<->")
            current=current.next
        print("None")
    
    def print_reverse(self):
        current=self.head
        while current.next:
            current=current.next
        while current:
            print(current.data,end="<-->")
            current=current.prev
        print("None")
        

dll=doublyLinkedlist()
for i in range(0,25,3):
    dll.append(i)
dll.printlist()
dll.print_reverse()
        
