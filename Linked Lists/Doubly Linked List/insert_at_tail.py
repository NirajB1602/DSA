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

def insertInTail(head,data):
    temp = Node(data)
    if head == None:
        return temp
        
    curr = head
    while curr.next != None:
        curr = curr.next
        
    curr.next = temp
    temp.prev = curr
    
    return head

head = Node(10)
head = insertInhead(head, 20)
head = insertInhead(head, 30)

insertInTail(head, 50)
displayList(head)

