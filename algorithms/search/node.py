class Node:
    data = None
    next = None
    
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
head = Node(1, None)

node = Node(4, None)
head.next = node

node2 = Node(5, None)
node.next = node2

temp = head
while(temp != None):
    print(temp.data)
    temp = temp.next
    