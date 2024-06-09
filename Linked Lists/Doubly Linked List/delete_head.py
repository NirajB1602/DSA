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

def deleteHead(head):
    if head == None or head.next == None:
        return None
        
    temp = head.next
    head.next = None
    temp.prev = None
    
    return temp

head = Node(10)
head = insertInhead(head, 20)
head = insertInhead(head, 30)

displayList(head)
lst = deleteHead(head)
print()
displayList(lst)