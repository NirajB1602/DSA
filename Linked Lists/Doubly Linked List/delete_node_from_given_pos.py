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

def deleteNode(head, pos):
    if pos == 1:
        head = head.next
        head.prev = None
        return head
            
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        if curr.next == None and i < (pos - 3):
            return head
            
    temp = curr.next
    curr.next = temp.next
    temp.prev = None
            
    if temp.next != None:
        temp.next.prev = curr
                
    return head

head = Node(10)
head = insertInhead(head, 20)
head = insertInhead(head, 30)

displayList(head)
lst = deleteNode(head, 2)
print()
displayList(lst)


