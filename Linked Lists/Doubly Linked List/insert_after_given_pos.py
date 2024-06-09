class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def displayList(head):
    if head == None:
        return None
        
    print(head.data)
    curr = head.next
    while curr != None:
        print(curr.data)
        curr = curr.next
        
def insertInhead(head,data):
    temp = Node(data)
    
    if head == None:
        return temp
        
    temp.next = head
    head.prev = temp
    return temp

def addNode(head, pos, data): # here we considered 0 based indexing instead of 1 based indexing, all other problems are done using 1 based indexing
    temp = Node(data)
    if pos == 0 and head.next == None:
        head.next = temp
        temp.prev = head
        return head
        
    curr = head
    for i in range(pos):
        curr = curr.next
        if curr == None and i < pos - 1:
            return head
        
    temp.next = curr.next
    
    if curr.next != None:
        curr.next.prev = temp
        
    curr.next = temp
    temp.prev = curr
    
    return head

head = Node(10)
head = insertInhead(head, 20)
head = insertInhead(head, 30)

addNode(head, 2, 100)

displayList(head)

